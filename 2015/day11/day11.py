#!/usr/bin/env python3

from typing import List


def increment_password(pw: List[str]):
    for i in range(len(pw) - 1, -1, -1):
        if pw[i] == 'z':
            pw[i] = 'a'
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break


def password_is_valid(pw: List[str]) -> bool:
    letter_pairs = set()
    straight = 1

    for i, c in enumerate(pw):
        if c in ['i', 'o', 'l']:
            return False

        if i > 0:
            if straight < 3:
                if ord(c) == ord(pw[i - 1]) + 1:
                    straight += 1
                else:
                    straight = 1

            if c == pw[i - 1]:
                letter_pairs.add(c)

    return straight == 3 and len(letter_pairs) >= 2


def next_password(pw: str) -> str:
    pw_list = [c for c in pw]

    while True:
        increment_password(pw_list)
        if all([d == 'z' for d in pw_list]):
            raise ValueError("passwords exhausted")

        if password_is_valid(pw_list):
            break

    return ''.join(pw_list)


if __name__ == '__main__':
    pw = input()

    next_pw = next_password(pw)
    next_next_pw = next_password(next_pw)

    print("The next valid password is '{}'.".format(next_pw))
    print("The next next valid password is '{}'.".format(next_next_pw))
