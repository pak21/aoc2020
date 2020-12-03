#!/usr/bin/env python3

import functools
import sys

with open(sys.argv[1]) as f:
    text = f.readlines()

trees = [[c == '#' for c in list(line.strip())] for line in text]

def check_slope(slope):
    pos = (0, 0)

    is_tree = []
    while pos[1] < len(trees):
        is_tree.append(trees[pos[1]][pos[0]])
        pos = ((pos[0] + slope[0]) % len(trees[0]), pos[1] + slope[1])
    return sum(is_tree)

counts = [check_slope(slope) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
print(counts)

product = functools.reduce(lambda a, b: a * b, counts, 1)
print(product)
