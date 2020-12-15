#!/usr/bin/env python3

import sys


class Found(Exception):
    """ dirty way used to exit multiples loop """


# read input file and transform each line into an integer
with open(sys.argv[1], "r") as f:
    expenses1 = list(map(int, f.readlines()))
    expenses2 = expenses1.copy()

# init
part1 = None
part2 = None

# part1
while part1 is None:
    i = expenses1.pop()
    for j in expenses1:
        if i + j == 2020:
            part1 = i * j

# part2
try:
    while part2 is None:
        i = expenses2.pop()
        for j in expenses2:
            for k in expenses2:
                if i + j + k == 2020:
                    part2 = i * j * k
                    raise Found
except Found:
    pass

# done
print(str(part1))
print(str(part2))
