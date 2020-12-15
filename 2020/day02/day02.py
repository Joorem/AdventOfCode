#!/usr/bin/env python3

import re
import sys


def get_elements(string: str) -> dict:
    """ analyse a string and return a dict with each elements matching a regex.
        example:
            {'n1': '4', 'n2': '5', 'letter': 'm', 'password': 'mmpth'}
    """

    p = re.match(r"(?P<n1>[0-9]+)-(?P<n2>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+)", string)

    return p.groupdict()


# read input file
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# init
part1 = 0
part2 = 0

# work
for line in lines:
    elements = get_elements(line)
    letter = str(elements["letter"])
    n1 = int(elements["n1"])
    n2 = int(elements["n2"])
    password = str(elements["password"])

    # part1
    if n1 <= password.count(letter) <= n2:
        part1 += 1

    # part2
    count = 0
    if password[n1 - 1] is letter:
        count += 1
    if password[n2 - 1] is letter:
        count += 1
    if count == 1:
        part2 += 1

# done
print(f"part1: {part1}")
print(f"part2: {part2}")
