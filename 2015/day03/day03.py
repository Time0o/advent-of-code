#!/usr/bin/env python3


def count_houses(inp: str) -> int:
    pos = (0, 0)

    visited = {pos}

    for c in inp:
        step = {
            '^': (1, 0),
            'v': (-1, 0),
            '>': (0, 1),
            '<': (0, -1)
        }[c]

        pos = (pos[0] + step[0], pos[1] + step[1])
        visited.add(pos)

    return len(visited)


def count_houses_robo_santa(inp: str) -> int:
    pos = (0, 0)
    pos_robo = (0, 0)

    visited = {pos}

    robo_turn = False
    for c in inp:
        step = {
            '^': (1, 0),
            'v': (-1, 0),
            '>': (0, 1),
            '<': (0, -1)
        }[c]

        if robo_turn:
            pos_robo = (pos_robo[0] + step[0], pos_robo[1] + step[1])
            visited.add(pos_robo)
        else:
            pos = (pos[0] + step[0], pos[1] + step[1])
            visited.add(pos)

        robo_turn = not robo_turn

    return len(visited)


if __name__ == '__main__':
    inp = input()

    fmt = "{} houses received at least one present (without robo santa)."
    print(fmt.format(count_houses(inp)))

    fmt = "{} houses received at least one present (with robo santa)."
    print(fmt.format(count_houses_robo_santa(inp)))
