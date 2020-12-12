#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    instructions = list(map(lambda l: (l[0], int(l[1:])), f.readlines()))

# Part 1

state = ((0, 0), 0)

DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]

ACTIONS = {
    'N': lambda s, v: ((s[0][0] - v, s[0][1]), s[1]),
    'S': lambda s, v: ((s[0][0] + v, s[0][1]), s[1]),
    'E': lambda s, v: ((s[0][0], s[0][1] + v), s[1]),
    'W': lambda s, v: ((s[0][0], s[0][1] - v), s[1]),
    'L': lambda s, v: ((s[0][0], s[0][1]), (s[1] + v // 90) % 4),
    'R': lambda s, v: ((s[0][0], s[0][1]), (s[1] - v // 90) % 4),
    'F': lambda s, v: ((s[0][0] + v * DIRECTIONS[s[1]][0], s[0][1] + v * DIRECTIONS[s[1]][1]), s[1])
}

for ins in instructions:
    state = ACTIONS[ins[0]](state, ins[1])
print(abs(state[0][0]) + abs(state[0][1]))

# Part 2

def rotate(angle, offset):
    diff = (angle // 90) % 4
    if diff == 0:
        return offset
    elif diff == 1:
        return (-offset[1], offset[0])
    elif diff == 2:
        return (-offset[0], -offset[1])
    elif diff == 3:
        return (offset[1], -offset[0])
    else:
        raise Exception(angle, offset)

ACTIONS2 = {
    'N': lambda s, v: (s[0], (s[1][0] - v, s[1][1])),
    'S': lambda s, v: (s[0], (s[1][0] + v, s[1][1])),
    'E': lambda s, v: (s[0], (s[1][0], s[1][1] + v)),
    'W': lambda s, v: (s[0], (s[1][0], s[1][1] - v)),
    'L': lambda s, v: (s[0], rotate(v, s[1])),
    'R': lambda s, v: (s[0], rotate(-v, s[1])),
    'F': lambda s, v: ((s[0][0] + v * s[1][0], s[0][1] + v * s[1][1]), s[1])
}

state2 = ((0, 0), (-1, 10))
for ins in instructions:
    state2 = ACTIONS2[ins[0]](state2, ins[1])
print(abs(state2[0][0]) + abs(state2[0][1]))
