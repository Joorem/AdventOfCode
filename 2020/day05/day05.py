#!/usr/bin/env python3

import sys

# read input file
with open(sys.argv[1], 'r') as fd:
    partitions = fd.readlines()

# init
part1 = 0
part2 = 0
seat_ids = []

# part1
for partition in partitions:
    # row
    left = 128
    row = 0
    for letter in partition[:7]:
        left = int(left / 2)
        if letter == "B":
            row += left

    # column
    column = 0
    left = 8
    for letter in partition[7:]:
        left = int(left / 2)
        if letter == "R":
            column += left

    # seat_id
    seat_ids.append(row * 8 + column)

part1 = max(seat_ids)

# part2
index = 0
seat_ids.sort()
for seat_id in seat_ids[0:len(seat_ids) - 1]:
    if seat_ids[index + 1] - seat_ids[index] > 1:
        part2 = seat_id + 1
        break
    index += 1

# done
print(f"part1: {part1}")
print(f"part2: {part2}")
