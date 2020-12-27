#!/usr/bin/env python3

import sys


def accumulate(instructions: list) -> dict:
    """
    Read and execute instructions until an infinite loop if found:
        acc +12 -> add 12 to 'acc'
        jmp +48 -> jump to the instruction located at 'index' + 48
        nop -56 -> do nothing & go to the next instruction

    if an instruction has already been executed, stop and return the current 'acc' value
    """

    acc = 0
    index = 0
    seen = []

    while index < len(instructions):
        if index in seen:
            return {'acc': acc, 'infinite': True}

        seen.append(index)
        op, val = instructions[index].split(' ')

        if op == 'acc':
            acc += int(val)
        elif op == 'jmp':
            index += int(val)
            continue

        index += 1

    return {'acc': acc, 'infinite': False}


# read input file
original_instructions = []
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        original_instructions.append(line.rstrip())

# init
part1 = 0
part2 = 0

# part1
part1 = accumulate(original_instructions)['acc']

# part2
swap = {'jmp': 'nop', 'nop': 'jmp'}

for i in range(0, len(original_instructions) - 1):
    modified_instructions = original_instructions.copy()
    operation, value = modified_instructions[i].split(' ')

    if operation in ('nop', 'jmp'):
        modified_instructions[i] = f"{swap[operation]} {value}"
        res = accumulate(modified_instructions)
        if res['infinite'] is False:
            part2 = res['acc']
            break

# done
print(f"part1: {part1}")
print(f"part2: {part2}")
