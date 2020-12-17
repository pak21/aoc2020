#!/usr/bin/env python3

import collections
import itertools
import sys

import numpy as np

dimensions = int(sys.argv[2])
generations = int(sys.argv[3])

active = set()
with open(sys.argv[1]) as f:
    for y, l in enumerate(f.readlines()):
        for x, c in enumerate(l.strip()):
            if c == '#':
                loc = [0] * dimensions
                loc[0] = x
                loc[1] = y
                active.add(tuple(loc))

STEPS = [-1, 0, 1]
zero_step = tuple([0] * dimensions)
DIRECTIONS = list(map(np.array, filter(lambda s: s != zero_step, itertools.product(*([STEPS] * dimensions)))))

def is_active(old, count):
    return count == 3 or (old and count == 2)

def iterate(state):
    counts = collections.defaultdict(int)
    for cell_tuple in state:
        cell = np.array(cell_tuple)
        for d in DIRECTIONS:
            counts[tuple(cell + d)] += 1

    next_active = set(map(lambda p: p[0], filter(lambda p: is_active(p[0] in state, p[1]), counts.items())))
    return next_active

for i in range(generations):
    active = iterate(active)

print(len(active))
