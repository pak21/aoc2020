#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    unpadded = list(map(lambda l: ['.'] + list(l.strip()) + ['.'], f.readlines()))

padding = ['.'] * len(unpadded[0])

state = [padding] + unpadded + [padding]

def dump_state(state):
    print('\n'.join(map(lambda l: ''.join(l), state)))

def evolve_cell(state, y, x):
    current = state[y][x]
    if current == '.':
        return '.'

    occupied = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            if state[y+dy][x+dx] == '#':
                occupied += 1

    if current == 'L':
        return '#' if occupied == 0 else 'L'

    return 'L' if occupied >= 4 else '#'

def iterate(state):
    next_state = []
    for y in range(len(state)):
        next_row = []
        for x in range(len(state[y])):
            next_row.append(evolve_cell(state, y, x))
        next_state.append(next_row)

    return next_state

def count_state(state):
    return sum(map(lambda r: sum(map(lambda c: c == '#', r)), state))

prev_count = -1

while False:
    state = iterate(state)
    count = count_state(state)
    if count == prev_count:
        break
    prev_count = count

#print(count)

def evolve_cell2(state, y, x):
    current = state[y][x]
    if current == '.':
        return '.'

    occupied = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            y2 = y + dy
            x2 = x + dx
            while y2 >= 0 and y2 < len(state) and x2 > 0 and x2 < len(state[0]):
                if state[y2][x2] == '#':
                    occupied += 1
                    break

                if state[y2][x2] == 'L':
                    break

                y2 += dy
                x2 += dx

    if current == 'L':
        return '#' if occupied == 0 else 'L'

    return 'L' if occupied >= 5 else '#'

def iterate2(state):
    next_state = []
    for y in range(len(state)):
        next_row = []
        for x in range(len(state[y])):
            next_row.append(evolve_cell2(state, y, x))
        next_state.append(next_row)

    return next_state

prev_count = -1
while True:
    state = iterate2(state)
    count = count_state(state)
    if count == prev_count:
        break
    prev_count = count

print(count)
