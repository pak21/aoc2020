#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    public_keys = list(map(int, f.readlines()))

def find(targets):
    x = 1
    loop_size = 1
    while True:
        x = (x * 7) % 20201227
        if x == targets[0]:
            return loop_size, targets[1]
        elif x == targets[1]:
            return loop_size, targets[0]
        loop_size += 1

loop_size, y = find(public_keys)

z = 1
for i in range(loop_size):
    z = (z * y) % 20201227

print(z)
