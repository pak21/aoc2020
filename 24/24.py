#!/usr/bin/env python3

import collections
import itertools
import sys

import numpy as np

DIRECTIONS = {
    'e': np.array([1, 0]),
    'ne': np.array([0, 1]),
    'nw': np.array([-1, 1]),
    'w': np.array([-1, 0]),
    'sw': np.array([0, -1]),
    'se': np.array([1, -1])
}

def parse_line(l):
    current = ''
    for c in l:
        current += c
        if c == 'e' or c == 'w':
            yield DIRECTIONS[current]
            current = ''

with open(sys.argv[1]) as f:
    ends = map(lambda l: tuple(sum(parse_line(l.strip()))), f.readlines())

active = set(map(lambda p: p[0], filter(lambda p: p[1] % 2 == 1, collections.Counter(ends).items())))

# Part 1

print(len(active))

# Part 2

def is_next_active(count, was_active):
    return count == 2 or (was_active and count == 1)

days = int(sys.argv[2])

for i in range(days):
    active = set(
        map(
            lambda p: p[0],
            filter(
                lambda p: p[1],
                map(
                    lambda p: (p[0], is_next_active(p[1], p[0] in active)),
                    collections.Counter(
                        map(
                            lambda p: tuple(np.array(p[0]) + p[1]),
                            itertools.product(active, DIRECTIONS.values())
                        )
                    ).items()
                )
            )
        )
    )
    print(len(active))
