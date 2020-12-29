#!/usr/bin/env python3
#
# Thanks to: https://github.com/mebeim/aoc, I learned a lot!

import sys
from copy import deepcopy

# read input file
with open(sys.argv[1], 'r') as fd:
    grid = list(map(list, map(str.rstrip, fd.readlines())))

# init
FLOOR, FREE, OCCUPIED = '.L#'
MAX_COL = len(grid[0]) - 1
MAX_ROW = len(grid) - 1
POSITIONS = ((-1, -1),  # Upper/Left
             (-1, 0),   # Upper
             (-1, 1),   # Upper/Right
             (0, -1),   # Left
             (0, 1),    # Right
             (1, -1),   # Lower/Left
             (1, 0),    # Lower
             (1, 1))    # Lower/Right
part1 = 0
part2 = 0


def apply_rules(source: list, f_count, tolerance: int = 4) -> int:
    while True:
        # because `source' is a list of list,
        # a shallow copy (source.copy() or source[:]) is not enough
        modified = deepcopy(source)
        for rawid, raw in enumerate(source):
            for colid, char in enumerate(raw):
                if char == FLOOR:
                    continue

                c = f_count(source, rawid, colid)
                if char == FREE and c == 0:
                    modified[rawid][colid] = OCCUPIED
                elif char == OCCUPIED and c >= tolerance:
                    modified[rawid][colid] = FREE

        if source == modified:
            return sum(row.count(OCCUPIED) for row in modified)

        source = modified


def count_occupied(s: list, row: int, column: int) -> int:
    count = 0
    for pr, pc in POSITIONS:
        nr, nc = row + pr, column + pc  # new row and new column to check
        if 0 <= nr <= MAX_ROW and 0 <= nc <= MAX_COL:  # check that we are in the grid
            count += s[nr][nc] == OCCUPIED

    return count


def count_occupied_in_sight(s: list, row: int, column: int) -> int:
    count = 0
    for pr, pc in POSITIONS:
        nr, nc = row + pr, column + pc  # new row and new column to check
        while 0 <= nr <= MAX_ROW and 0 <= nc <= MAX_COL:  # check that we are in the grid
            if s[nr][nc] != FLOOR:
                if s[nr][nc] == OCCUPIED:
                    count += 1
                break
            # continue to move in the same direction:
            nr += pr
            nc += pc

    return count


# part1
part1 = apply_rules(grid, count_occupied)

# part2
part2 = apply_rules(grid, count_occupied_in_sight, 5)

# done
print(f"part1: {part1}")
print(f"part2: {part2}")
