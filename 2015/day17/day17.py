#!/usr/bin/env python3

import sys
from typing import List

LITERS = 150


def find_combinations(buckets: List[int],
                      target: int,
                      size: int,
                      sizes: List[int]) -> int:
    if not buckets:
        return 0

    head, tail = buckets[0], buckets[1:]

    if head > target:
        res = 0
    elif head == target:
        res = 1
        sizes.append(size + 1)
    else:
        res = find_combinations(tail, target - head, size + 1, sizes)

    return res + find_combinations(tail, target, size, sizes)


if __name__ == '__main__':
    buckets = [int(b) for b in sys.stdin.read().split()]

    sizes = []
    combinations = find_combinations(buckets, LITERS, 0, sizes)

    min_buckets = min(sizes)
    num_min_buckets = sizes.count(min_buckets)

    fmt = "{} combinations can fit {} liters of eggnog."
    print(fmt.format(combinations, LITERS))

    fmt = "{} combinations use only {} buckets."
    print(fmt.format(num_min_buckets, min_buckets))
