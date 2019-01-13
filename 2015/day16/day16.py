#!/usr/bin/env python3

import re
import sys
from operator import eq, gt, lt
from typing import Dict, List

TARGET = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

TARGET_RELATIONS = {
    'children': eq,
    'cats': gt,
    'samoyeds': eq,
    'pomeranians': lt,
    'akitas': eq,
    'vizslas': eq,
    'goldfish': lt,
    'trees': gt,
    'cars': eq,
    'perfumes': eq
}


def find_aunt(aunts: List[Dict[str, int]],
              target: Dict[str, int],
              use_relations: bool = False) -> int:

    for i, aunt in enumerate(aunts):
        match = True
        for k, v in aunt.items():
            if use_relations:
                if not TARGET_RELATIONS[k](v, target[k]):
                    match = False
                    break
            else:
                if v != target[k]:
                    match = False
                    break

        if match:
            return i + 1


if __name__ == '__main__':
    aunts = []

    for line in sys.stdin:
        line = line.rstrip()

        properties = re.findall(r'(\w+): (\d+)', line)
        aunts.append(dict(map(lambda p: (p[0], int(p[1])), properties)))

    fmt = "The correct aunt is Sue no. {}."
    print(fmt.format(find_aunt(aunts, TARGET)))

    fmt = "No, actually the correct aunt is Sue no. {}."
    print(fmt.format(find_aunt(aunts, TARGET, use_relations=True)))
