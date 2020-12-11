#!/usr/bin/env python3

import sys

part = int(sys.argv[2])

with open(sys.argv[1]) as f:
    unpadded = list(map(lambda l: ['.'] + list(l.strip()) + ['.'], f.readlines()))

padding = ['.'] * len(unpadded[0])

state = [padding] + unpadded + [padding]

def dump_state(state):
    print('\n'.join(map(lambda l: ''.join(l), state)))

def evaluate_neighbour2(state, y, x, dy, dx):
    y2 = y + dy
    x2 = x + dx
    while y2 >= 0 and y2 < len(state) and x2 > 0 and x2 < len(state[0]):
        if state[y2][x2] == '#':
            return True

        if state[y2][x2] == 'L':
            return False

        y2 += dy
        x2 += dx

    return False

def evolve_cell(state, y, x, evaluate_fn, threshold):
    current = state[y][x]
    if current == '.':
        return '.'

    occupied = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            occupied += evaluate_fn(state, y, x, dy, dx)

    next_occupied = (occupied == 0) if current == 'L' else (occupied < threshold)
    return '#' if next_occupied else 'L'

def iterate(state, evaluate_fn, threshold):
    next_state = []
    for y in range(len(state)):
        next_row = []
        for x in range(len(state[y])):
            next_row.append(evolve_cell(state, y, x, evaluate_fn, threshold))
        next_state.append(next_row)

    return next_state

def count_state(state):
    return sum(map(lambda r: sum(map(lambda c: c == '#', r)), state))

evaluate_fn, threshold = (lambda s, y, x, dy, dx: s[y+dy][x+dx] == '#', 4) if part == 1 else (evaluate_neighbour2, 5)

prev_count = -1
while True:
    state = iterate(state, evaluate_fn, threshold)
    count = count_state(state)
    if count == prev_count:
        break
    prev_count = count
print(count)
