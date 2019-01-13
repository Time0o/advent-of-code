#!/usr/bin/env python3

import re
import sys
from typing import Dict, Tuple

SECONDS = 2503


def dict_argmax(d: Dict[str, int]) -> Tuple[str, int]:
    v_max, k_max = max([(v, k) for k, v in d.items()])

    return k_max, v_max


def get_distance(speed: int, flight: int, rest: int, seconds: int) -> int:
    dist = seconds // (flight + rest) * (speed * flight)
    dist += speed * min(seconds % (flight + rest), flight)

    return dist


def max_distance(reindeers: Dict[str, Tuple[int, int, int]],
                 seconds: int) -> Tuple[str, int]:

    distances = {}
    for name, stats in reindeers.items():
        distances[name] = get_distance(*stats, seconds)

    return dict_argmax(distances)


def max_points(reindeers: Dict[str, Tuple[int, int, int]],
               seconds: int) -> Tuple[str, int]:

    distances = {}
    points = {}

    for s in range(seconds):
        for name, (speed, flight, rest) in reindeers.items():
            distances[name] = get_distance(speed, flight, rest, s)

        name, _ = dict_argmax(distances)

        points[name] = points.get(name, 0) + 1

    return dict_argmax(points)


if __name__ == '__main__':
    reg = re.compile(r'^(\w+) can fly (\d+) km/s for (\d+) seconds,'
                     r' but then must rest for (\d+) seconds\.$')

    reindeers = {}
    for line in sys.stdin:
        name, speed, flight, rest = reg.match(line.rstrip()).groups()

        reindeers[name] = tuple(map(int, (speed, flight, rest)))

    fmt = "The fastest reindeer, {}, travels {} km in {} seconds."
    print(fmt.format(*max_distance(reindeers, SECONDS), SECONDS))

    fmt = "Reindeer {} has accumulated the most points ({})."
    print(fmt.format(*max_points(reindeers, SECONDS)))
