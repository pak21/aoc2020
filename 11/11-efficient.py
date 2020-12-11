#!/usr/bin/env python3

import sys

part = int(sys.argv[2])

# Some tedious processing to convert the input into the set of (y, x) pairs which contain a seat

with open(sys.argv[1]) as f:
    seats_list = enumerate(
        map(
            lambda r: map(
                lambda p: p[0],
                filter(
                    lambda p: p[1] == 'L',
                    enumerate(r.strip())
                )
            ),
            f.readlines()
        )
    )

seats = set(item for sublist in map(lambda p: map(lambda x: (p[0], x), p[1]), seats_list) for item in sublist)

# Now for each seat, find its neighbours

DIRECTIONS = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

neighbours = list(map(
    lambda s: (s, list(filter(
        lambda s2: s2 in seats,
        map(lambda d: (s[0] + d[0], s[1] + d[1]), DIRECTIONS)))),
    seats
))

# TODO: create the second neighbour map for Part 2

# Now we can iterate

def is_occupied_next(currently_occupied, neighbours):
    return neighbours < 4 if currently_occupied else neighbours == 0

occupied = set()
prev_count = 0

while True:
    occupied = set(map(
        lambda p: p[0],
        filter(
            lambda p: p[1],
            map(
                lambda p: (p[0], is_occupied_next(p[0] in occupied, sum(map(lambda n: n in occupied, p[1])))),
                neighbours
            )
        )
    ))
    count = len(occupied)
    if count == prev_count:
        break
    prev_count = count

print(len(occupied))

# tl;dr: this isn't that much more efficient, only about 4x or so quicker than the original
# Not going to bother to implement Part 2
