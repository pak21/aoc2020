#!/usr/bin/env python3

import sys

class Cup:
    def __init__(self, cup_id):
        self.cup_id = cup_id

with open(sys.argv[1]) as f:
    starting_ids = list(map(int, f.readline().strip()))

moves = int(sys.argv[2])
max_cup = int(sys.argv[3])

cups = list(map(Cup, range(max_cup+1)))

first = cups[starting_ids[0]]
prev = first
for i in starting_ids[1:]:
    cup = cups[i]
    prev.next_cup = cup
    prev = cup

for i in range(len(starting_ids)+1, max_cup+1):
    cup = cups[i]
    prev.next_cup = cup
    prev = cup

cup.next_cup = first

current = first
for m in range(moves):
    picked_up = current.next_cup
    current.next_cup = picked_up.next_cup.next_cup.next_cup

    picked_up_ids = {
        picked_up.cup_id,
        picked_up.next_cup.cup_id,
        picked_up.next_cup.next_cup.cup_id
    }

    destination = current.cup_id
    while True:
        destination = (destination - 1)
        if destination == 0:
            destination = max_cup
        if destination not in picked_up_ids:
            break

    target = cups[destination]
    picked_up.next_cup.next_cup.next_cup = target.next_cup
    target.next_cup = picked_up

    current = current.next_cup

a = cups[1].next_cup
b = a.next_cup

print(a.cup_id, b.cup_id, a.cup_id * b.cup_id)
