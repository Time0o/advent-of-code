#!/usr/bin/env python3

import math
import re
import sys
from itertools import permutations
from typing import Dict, Tuple


def sort_tuple(tup: tuple) -> tuple:
    return tuple(sorted(tup))


def extreme_routes(distances: Dict[Tuple[str, str], int]) -> Tuple[int, int]:
    locations = set()
    for loc1, loc2 in distances.keys():
        locations.update([loc1, loc2])

    min_dist = math.inf
    max_dist = 0
    for path in permutations(locations):
        dist = 0
        for endpoints in zip(path[:-1], path[1:]):
            dist += distances[sort_tuple(endpoints)]

        min_dist = min(min_dist, dist)
        max_dist = max(max_dist, dist)

    return min_dist, max_dist


if __name__ == '__main__':
    reg = re.compile(r'(\w+) to (\w+) = (\d+)')

    distances = {}
    for line in sys.stdin:
        loc1, loc2, dist = reg.match(line.rstrip()).groups()

        distances[sort_tuple((loc1, loc2))] = int(dist)

    min_dist, max_dist = extreme_routes(distances)
    print("Shortest route has length {}.".format(min_dist))
    print("Longest route has length {}.".format(max_dist))
