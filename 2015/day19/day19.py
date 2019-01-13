#!/usr/bin/env python3

import sys
from typing import List, Tuple


def count_modifications(molecule: str,
                        replacements: List[Tuple[str, str]]) -> int:

    modifications = set()
    for source, target in replacements:
        i = 0
        while i < len(molecule):
            try:
                j = molecule[i:].index(source) + i
                mod = molecule[:j] + target + molecule[(j + len(source)):]
                modifications.add(mod)
                i = j + len(source)
            except ValueError:
                break

    return len(modifications)


if __name__ == '__main__':
    replacements = []

    read_molecule = False
    for line in sys.stdin:
        line = line.rstrip()

        if read_molecule:
            molecule = line
            break
        elif not line:
            read_molecule = True
        else:
            replacements.append(line.rstrip().split(' => '))

    fmt = "{} distinct molecules can be created."
    print(fmt.format(count_modifications(molecule, replacements)))
