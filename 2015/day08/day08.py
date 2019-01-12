#!/usr/bin/env python3

import sys


def in_memory_size(sequence: str) -> int:
    size = 0

    i = 1
    while i < len(sequence) - 1:
        if sequence[i] == '\\':
            escaped = sequence[i + 1]

            if escaped in ['\\', '"']:
                size += 1
                i += 1
            elif escaped == 'x':
                size += 1
                i += 3
            else:
                fmt = "invalid escape sequence: {}"
                raise ValueError(fmt.format(sequence[i:(i + 1)]))
        else:
            size += 1

        i += 1

    return size


def encode(sequence: str) -> str:
    sequence = sequence.replace('\\', '\\\\')
    sequence = sequence.replace('"', '\\"')

    return '"{}"'.format(sequence)


if __name__ == '__main__':
    code_size = 0
    mem_size = 0
    repr_size = 0

    for string in sys.stdin:
        string = string.rstrip()

        code_size += len(string)
        mem_size += in_memory_size(string)
        repr_size += len(encode(string))

    fmt = "Literal vs. in memory character difference is {}."
    print(fmt.format(code_size - mem_size))

    fmt = "Encoded vs. literal character difference is {}."
    print(fmt.format(repr_size - code_size))
