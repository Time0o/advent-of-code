#!/usr/bin/env python3

import math
import re
import sys
from itertools import permutations
from typing import Dict, Set, Tuple


def optimal_happiness(persons: Set[str],
                      happiness: Dict[Tuple[str, str], int]) -> int:

    head = min(persons)

    rest = persons.copy()
    rest.remove(head)

    optimum = -math.inf
    for seating in permutations(rest):
        seating = list(seating)

        val = 0
        for neighbours in zip([head] + seating, seating + [head]):
            val += happiness[neighbours]
            val += happiness[tuple(reversed(neighbours))]

        optimum = max(optimum, val)

    return optimum


if __name__ == '__main__':
    reg = re.compile(r'^(\w+) would (gain|lose)'
                      ' (\d+) happiness units'
                      ' by sitting next to (\w+)\.$')

    persons = set()
    happiness = {}
    for line in sys.stdin:
        person1, sign, points, person2 = reg.match(line.rstrip()).groups()
        points = int(points) if sign == 'gain' else -int(points)

        persons.update([person1, person2])

        happiness[(person1, person2)] = points

    optimum1 = optimal_happiness(persons, happiness)

    for person in persons:
        happiness[('me', person)] = 0
        happiness[(person, 'me')] = 0

    persons.add('me')

    optimum2 = optimal_happiness(persons, happiness)

    print("Optimal happiness is {}.".format(optimum1))
    print("Optimal happiness (including myself) is {}.".format(optimum2))
