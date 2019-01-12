#!/usr/bin/env python3


def final_floor(instr: str) -> int:
    res = 0
    for c in instr:
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
        else:
            raise ValueError('invalid character')

    return res


def basement_index(instr: str) -> int:
    res = 0
    for i, c in enumerate(instr):
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
        else:
            raise ValueError('invalid character')

        if res == -1:
            return i + 1

    return 0


if __name__ == '__main__':
    instr = input()

    print("Final floor is {}.".format(final_floor(instr)))
    print("Basement index is {}.".format(basement_index(instr)))
