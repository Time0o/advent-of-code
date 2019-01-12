#!/usr/bin/env python3

from hashlib import md5

HASH_PREFIX1 = '00000'
HASH_PREFIX2 = '000000'


def find_hash_suffix(inp: str, prefix: str) -> int:
    i = 0
    while True:
        digest = md5((inp + str(i)).encode('utf-8')).hexdigest()
        if digest[:len(prefix)] == prefix:
            break

        i += 1

    return i


if __name__ == '__main__':
    inp = input()

    for prefix in HASH_PREFIX1, HASH_PREFIX2:
        fmt = "Lowest number which produces suitable hash with prefix '{}' is {}."
        print(fmt.format(prefix, find_hash_suffix(inp, prefix)))
