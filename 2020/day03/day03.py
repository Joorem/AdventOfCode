#!/usr/bin/env python3

import sys


def slope(right: int, down: int) -> int:
    """ count the number of trees encountered """
    count_trees = 0
    position = 0
    for line in FOREST_MAP[::down]:
        if line[position] == '#':
            count_trees += 1
        position = (position + right) % LINE_LENGTH

    return count_trees


# read input file
with open(sys.argv[1], 'r') as f:
    FOREST_MAP = f.read().splitlines()

# init
LINE_LENGTH = len(FOREST_MAP[0])

# part1
print(slope(3, 1))

# part2
print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
