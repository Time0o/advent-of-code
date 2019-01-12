#!/usr/bin/env python3

import re
import sys
from itertools import combinations
from math import inf


def wrapping_area(l: int, w: int, h: int) -> int:
    sides = (l * w, w * h, h * l)

    return sum(2 * s for s in sides) + min(sides)


def ribbon_length(l: int, w: int, h: int) -> int:
    min_perimeter = inf
    for d1, d2 in combinations((l, w, h), 2):
        min_perimeter = min(min_perimeter, 2 * d1 + 2 * d2)

    return min_perimeter + l * w * h


if __name__ == '__main__':
    paper_to_order = 0
    ribbon_to_order = 0

    reg = re.compile(r'^(\d+)x(\d+)x(\d+)$')
    for line in sys.stdin:
        l, w, h = map(int, reg.match(line.rstrip()).groups())

        paper_to_order += wrapping_area(l, w, h)
        ribbon_to_order += ribbon_length(l, w, h)

    print("Square feet of paper to order: {}.".format(paper_to_order))
    print("Feet of ribbon to order: {}.".format(ribbon_to_order))
