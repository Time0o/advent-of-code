#!/usr/bin/env python3

import json


def add_numbers(data, ignore_red: bool = False) -> int:
    if isinstance(data, dict):
        if ignore_red and ('red' in data.keys() or 'red' in data.values()):
            return 0

        return sum([add_numbers(k, ignore_red) + add_numbers(v, ignore_red)
                    for k, v in data.items()])

    if isinstance(data, list):
        return sum([add_numbers(e, ignore_red) for e in data])

    elif isinstance(data, int):
        return data

    else:
        return 0


if __name__ == '__main__':
    data = json.loads(input())

    sum_numbers = add_numbers(data)
    sum_numbers_no_red = add_numbers(data, ignore_red=True)

    fmt = "Sum of all numbers is {}."
    print(fmt.format(sum_numbers))

    fmt = "Sum of all numbers is {} (without dictionaries containing 'red')."
    print(fmt.format(sum_numbers_no_red))
