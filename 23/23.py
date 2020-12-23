#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    cups = list(map(int, f.readline().strip()))

moves = int(sys.argv[2])

print(cups)

n_cups = len(cups)

for m in range(moves):
    destination = cups[0]
    removed = cups[1:4]
    cups = cups[4:n_cups] + cups[0:1]

    print(cups)

    while True:
        destination -= 1
        if destination == 0:
            destination = n_cups
        if destination in cups:
            dest_index = cups.index(destination)
            break

    print('Destination', destination, '@', dest_index)

    cups = cups[0:dest_index+1] + removed + cups[dest_index+1:n_cups]
    print(cups)

one_index = cups.index(1)
print(''.join(map(str, cups[one_index+1:n_cups] + cups[0:one_index])))
