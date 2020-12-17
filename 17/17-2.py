#!/usr/bin/env python3

import collections
import itertools
import sys

active = set()
with open(sys.argv[1]) as f:
    y = 0
    for l in f.readlines():
        x = 0
        for c in l.strip():
            if c == '#':
                active.add((x, y, 0, 0))
            x = x + 1
        y = y + 1

STEPS = [-1, 0, 1]

DIRECTIONS = list(filter(lambda s: s != (0, 0, 0, 0), itertools.product(STEPS, STEPS, STEPS, STEPS)))

def is_active(old, count):
    if old:
        return count == 2 or count == 3
    else:
        return count == 3

def iterate(state):
    counts = collections.defaultdict(int)
    for cell in state:
        for d in DIRECTIONS:
            new_x, new_y, new_z, new_a = cell[0] + d[0], cell[1] + d[1], cell[2] + d[2], cell[3] + d[3]
            counts[(new_x, new_y, new_z, new_a)] += 1

    next_active = set(map(lambda p: p[0], filter(lambda p: is_active(p[0] in state, p[1]), counts.items())))
    return next_active

for i in range(6):
    active = iterate(active)

print(len(active))
