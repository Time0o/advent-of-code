#!/usr/bin/env python3

import re
import sys
from typing import List

TEASPOONS = 100
CALORIES = 500


def optimal_ingredients(ingredients: List[str],
                        teaspoons: int,
                        calories: int = None) -> int:
    max_score = 0
    for c1 in range(TEASPOONS + 1):
        for c2 in range(TEASPOONS - c1 + 1):
            for c3 in range(TEASPOONS - c1 - c2 + 1):
                c4 = TEASPOONS - c1 - c2 - c3

                sums = [max(0, c1 * i1 + c2 * i2 + c3 * i3 + c4 * i4)
                        for i1, i2, i3, i4 in zip(*ingredients)]

                if calories is not None and sums[-1] != calories:
                    continue

                score = 1
                for s in sums[:-1]:
                    score *= s

                max_score = max(max_score, score)

    return max_score


if __name__ == '__main__':
    reg = re.compile(r'^(\w+): '
                     r'capacity (-?\d+), '
                     r'durability (-?\d+), '
                     r'flavor (-?\d+), '
                     r'texture (-?\d+), '
                     r'calories (-?\d+)$')

    ingredients = []
    for line in sys.stdin:
        m = reg.match(line.rstrip())
        ingredient = m.group(1)
        cap, dur, flav, text, cal = map(int, m.groups()[1:])

        ingredients.append((cap, dur, flav, text, cal))

    score1 = optimal_ingredients(ingredients, TEASPOONS)
    score2 = optimal_ingredients(ingredients, TEASPOONS, calories=CALORIES)

    fmt = "Score of best recipe is {}."
    print(fmt.format(score1))

    fmt = "Score of best recipe with {} calories is {}."
    print(fmt.format(CALORIES, score2))
