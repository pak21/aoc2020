#!/usr/bin/env python3

import re
import sys

d = {}
passports = [d]
with open(sys.argv[1]) as f:
    for line in (l.strip() for l in f):
        if line == '':
            d = {}
            passports.append(d)
        else:
            d.update([s.split(':') for s in line.split(' ')])

def hgt(s):
    match = re.search(r'^([0-9]+)(cm|in)$', s)
    if not match:
        return False
    t, unit = match.groups()
    n = int(t)
    if unit == 'cm':
        return n >= 150 and n <= 193
    else:
        return n >= 59 and n <= 76

VALIDATORS = {
    'byr': lambda s: int(s) >= 1920 and int(s) <= 2002,
    'iyr': lambda s: int(s) >= 2010 and int(s) <= 2020,
    'eyr': lambda s: int(s) >= 2020 and int(s) <= 2030,
    'hgt': lambda s: hgt(s),
    'hcl': lambda s: re.search(r'^#[0-9a-f]{6}$', s) != None,
    'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda s: re.search(r'^[0-9]{9}$', s) != None
}

part1 = list(filter(lambda p: all(map(lambda k: k in p, VALIDATORS.keys())), passports))
part2 = list(filter(lambda p: all(map(lambda k: VALIDATORS[k](p[k]), VALIDATORS.keys())), part1))

print(len(part1), len(part2))
