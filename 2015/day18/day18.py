#!/usr/bin/env python3

import sys
from itertools import product
from typing import List

GRIDSIZE = [100, 100]
STEPS = 100


def next_state(on: bool, neighbours_on: int) -> bool:
    if on:
        return neighbours_on in (2, 3)
    else:
        return neighbours_on == 3


def update(light_grid: List[List[bool]], fix_corners: bool) -> List[List[bool]]:
    updated_light_grid = [row[:] for row in light_grid]

    for row in range(len(light_grid)):
        if fix_corners and row in (0, len(light_grid) - 1):
            cols = range(1, len(light_grid[0]) - 1)
        else:
            cols = range(len(light_grid[0]))

        for col in cols:
            neighbours_on = 0
            for offs_row, offs_col in product((-1, 0, 1), repeat=2):
                if offs_row == offs_col == 0:
                    continue

                row_ = row + offs_row
                if row_ < 0 or row_ > len(light_grid) - 1:
                    continue

                col_ = col + offs_col
                if col_ < 0 or col_ > len(light_grid[0]) - 1:
                    continue

                if light_grid[row_][col_]:
                    neighbours_on += 1

            updated_light_grid[row][col] = \
                next_state(light_grid[row][col], neighbours_on)

    return updated_light_grid


def simulate(light_grid: List[List[bool]],
             fix_corners: bool = False) -> List[List[bool]]:

    light_grid_copy = [row[:] for row in light_grid]

    if fix_corners:
        for row_corner, col_corner in product([0, -1], repeat=2):
            light_grid_copy[row_corner][col_corner] = True

    for _ in range(STEPS):
        light_grid_copy = update(light_grid_copy, fix_corners)

    return light_grid_copy


def count_lights(light_grid: List[List[bool]]) -> int:
    return sum([sum(row) for row in light_grid])


if __name__ == '__main__':
    light_grid = [[False] * GRIDSIZE[1] for _ in range(GRIDSIZE[0])]

    for i, line in enumerate(sys.stdin):
        for j, c in enumerate(line.rstrip()):
            if c == '#':
                light_grid[i][j] = True

    light_grid1 = simulate(light_grid)
    light_grid2 = simulate(light_grid, fix_corners=True)

    fmt = "Total number of lights turned on after {} steps is {}."
    print(fmt.format(STEPS, count_lights(light_grid1)))

    fmt = "And with fixed corners the number is {}."
    print(fmt.format(count_lights(light_grid2)))
