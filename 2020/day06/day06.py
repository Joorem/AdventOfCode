#!/usr/bin/env python3

import string
import sys

# read input file
with open(sys.argv[1], 'r') as fd:
    groups_answers = fd.read().split("\n\n")

# init
part1 = 0
part2 = 0

for answers in groups_answers:
    # part1
    ids = []
    for letter in answers:
        if letter.isalpha() and letter not in ids:
            ids.append(letter)
    part1 += len(ids)

    # part2
    tmp = string.ascii_lowercase
    for answer in answers.splitlines():
        tmp = list(set(answer) & set(tmp))
    part2 += len(tmp)

# done
print(f"part1: {part1}")
print(f"part2: {part2}")
