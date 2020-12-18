#!/usr/bin/env python3

import re
import sys


def str_to_dict(input_list: list) -> list:
    """
    Analyze a list of strings and return a list of dict with all found fields
    example:
        from:
            ['eyr:2028 iyr:2016 byr:1995 ecl:oth pid:543685203 hcl:#c0946f hgt:152cm cid:252']
        to:
            [{'byr': '1995', 'iyr': '2016', 'eyr': '2028', 'hgt': '152cm', 'hcl': '#c0946f', 'ecl': 'oth', 'pid': '543685203', 'cid': '252'}]
    """

    fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')
    list_of_dict = list()

    for info in input_list:
        tmp_dict = dict()
        for field in fields:
            search = re.search(rf"{field}:([a-z0-9#]+)", info)
            if search:
                tmp_dict[field] = search.group(1)
        if len(tmp_dict) >= 7:
            list_of_dict.append(tmp_dict)

    return list_of_dict


def is_valid(f: dict) -> bool:
    """ Compare an f to the policy """
    BYR_MIN = 1920
    BYR_MAX = 2002
    ECL_VAL = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    IYR_MIN = 2010
    IYR_MAX = 2020
    EYR_MIN = 2020
    EYR_MAX = 2030
    HCL_REG = r"^#[0-9a-f]{6}$"
    HGT_CM_MIN = 150
    HGT_CM_MAX = 193
    HGT_IN_MIN = 59
    HGT_IN_MAX = 76
    HGT_REG = r"^([0-9]{2,3})(in|cm)$"
    PID_REG = r"^[0-9]{9}$"

    if not BYR_MIN <= int(f['byr']) <= BYR_MAX:
        return False
    if not IYR_MIN <= int(f['iyr']) <= IYR_MAX:
        return False
    if not EYR_MIN <= int(f['eyr']) <= EYR_MAX:
        return False
    if not re.match(HCL_REG, f['hcl']):
        return False
    if f['ecl'] not in ECL_VAL:
        return False
    if not re.match(PID_REG, f['pid']):
        return False
    hgt = re.match(HGT_REG, f['hgt'])
    if hgt:
        height = int(hgt.group(1))
        unit = hgt.group(2)
        if unit == 'in':
            if not HGT_IN_MIN <= height <= HGT_IN_MAX:
                return False
        else:
            if not HGT_CM_MIN <= height <= HGT_CM_MAX:
                return False
    else:
        return False

    return True


# read input file
with open(sys.argv[1], 'r') as fd:
    input_content = fd.read().split("\n\n")

# init
part1 = 0
part1_list = list()
part2 = 0

# part1
for entry in str_to_dict(input_content):
    size_entry = len(entry)

    if size_entry == 8 or 'cid' not in entry:
        part1 += 1
        part1_list.append(entry)

# part2
for entry in part1_list:
    if is_valid(entry):
        part2 += 1

# done
print(f"part1: {part1}")
print(f"part2: {part2}")
