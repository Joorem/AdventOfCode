#!/usr/bin/env python3

import sys


def summable(number: int, numbers: list) -> bool:
    """
    Look for two entries in 'numbers' that sum to 'number'
    """

    while len(numbers) > 0:
        number1 = numbers.pop()
        for number2 in numbers:
            if number1 + number2 == number:
                return True

    return False


# read input file
xmas_data = []
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        xmas_data.append(int(line.rstrip()))

# init
PREAMBLE = 25
part1 = 0
part2 = 0

# part1
for index in range(PREAMBLE, len(xmas_data) - 1):
    if not summable(xmas_data[index], xmas_data[index - 25:index]):
        part1 = xmas_data[index]
        break

# part2
i = 0
while part2 == 0 and i < len(xmas_data) - 1:
    j = i + 1
    while i < j < len(xmas_data):
        if sum(xmas_data[i:j]) == part1:
            part2 = min(xmas_data[i:j]) + max(xmas_data[i:j])
            break
        j += 1
    i += 1

# done
print(f"part1: {part1}")
print(f"part2: {part2}")
