#!/usr/bin/env python3

import sys


def is_nice(string: str) -> bool:
    vowel_count = 0
    double_letter = False

    for i, c in enumerate(string):
        if c in 'aeiou':
            vowel_count += 1

        if i > 0:
            if not double_letter and string[i - 1] == c:
                double_letter = True

            forbidden_previous = {
                'b': 'a',
                'd': 'c',
                'q': 'p',
                'y': 'x'
            }.get(c)

            if string[i - 1] == forbidden_previous:
                return False

    return vowel_count >= 3 and double_letter


def is_nice2(string: str) -> bool:
    spaced_double_letter = False
    double_letter_pair = False

    letter_pairs = {}
    for i in range(len(string)):
        if not double_letter_pair and i > 0:
            cc = string[(i - 1):(i + 1)]

            if cc in letter_pairs:
                if letter_pairs[cc] != i - 1:
                    double_letter_pair = True
            else:
                letter_pairs[cc] = i

        if not spaced_double_letter and i > 1:
            if string[i - 2] == string[i]:
                spaced_double_letter = True

        if double_letter_pair and spaced_double_letter:
            return True

    return False


if __name__ == '__main__':
    nice_strings = 0
    nice_strings2 = 0

    for string in sys.stdin:
        if is_nice(string.rstrip()):
            nice_strings += 1

        if is_nice2(string.rstrip()):
            nice_strings2 += 1

    print("Number of nice strings is {}/{}.".format(nice_strings, nice_strings2))
