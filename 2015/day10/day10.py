#!/usr/bin/env python3

from typing import List

ITERATIONS = [40, 50]


def look_and_say(seq: List[int]) -> List[int]:
    res = []

    i = 0
    j = 0
    while j <= len(seq):
        if j == len(seq) or seq[j] != seq[i]:
            res += [j - i, seq[i]]
            i = j

        j += 1

    return res


if __name__ == '__main__':
    seq = [int(c) for c in input()]

    iterations_total = 0
    for iterations in ITERATIONS:
        for _ in range(iterations - iterations_total):
            seq = look_and_say(seq)

        iterations_total += iterations

        fmt = "Result has length {} after {} iterations"
        print(fmt.format(len(seq), iterations))
