#!/usr/bin/env python3

import collections
import itertools
import sys

import numpy as np

DIRECTIONS = {
    'e': (1, 0),
    'ne': (0, 1),
    'nw': (-1, 1),
    'w': (-1, 0),
    'sw': (0, -1),
    'se': (1, -1)
}

def parse_line(l):
    current = ''
    for c in l:
        current += c
        if c == 'e' or c == 'w':
            yield np.array(DIRECTIONS[current])
            current = ''

with open(sys.argv[1]) as f:
    active = set(
        map(
            lambda p: p[0],
            filter(
                lambda p: p[1] % 2 == 1,
                collections.Counter(
                    map(
                        lambda l: tuple(sum(parse_line(l.strip()))),
                        f.readlines()
                    )
                ).items()
            )
        )
    )

# Part 1

print(len(active))

# Part 2

for i in range(int(sys.argv[2])):
    active = set(
        map(
            lambda p: p[0],
            filter(
                lambda p: p[1],
                map(
                    lambda p: (p[0], p[1] == 2 or (p[0] in active and p[1] == 1)),
                    collections.Counter(
                        map(
                            lambda p: (p[0][0] + p[1][0], p[0][1] + p[1][1]),
                            itertools.product(active, DIRECTIONS.values())
                        )
                    ).items()
                )
            )
        )
    )

print(len(active))
