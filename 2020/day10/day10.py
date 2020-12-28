#!/usr/bin/env python3

from functools import cache
import sys


@cache  # Memoization is crucial here as we use a lot of recursion
def combinaisons(index: int) -> int:
    if index == len(joltages) - 1:
        return 1

    res = 0
    for j in range(index + 1, min(index + 4, len(joltages))):
        if 0 < joltages[j] - joltages[index] < 4:
            res += combinaisons(j)

    return res


# read input file
joltages = [0]  # the charging outlet near our seat has an effective joltage rating of 0
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        joltages.append(int(line.rstrip()))
joltages.append(max(joltages) + 3)  # our device's built-in adapter is always 3 higher than the highest adapter
joltages.sort()

# init
part1 = 0
part2 = 0

# part1
diff_1_jolt = 0
diff_3_jolt = 0

for jolt in joltages:
    if jolt + 1 in joltages:
        diff_1_jolt += 1
    elif jolt + 3 in joltages:
        diff_3_jolt += 1

part1 = diff_1_jolt * diff_3_jolt

# part2
part2 = combinaisons(0)

# done
print(f"part1: {part1}")
print(f"part2: {part2}")
