#!/usr/bin/env python3

import sys

turns = int(sys.argv[2])

with open(sys.argv[1]) as f:
    numbers = dict(map(lambda p: (p[1], p[0]), enumerate(map(int, f.read().split(',')))))

last_spoken_diff = 0
for i in range(len(numbers), turns):
    last_spoken = last_spoken_diff
    last_spoken_diff = i - numbers[last_spoken] if last_spoken in numbers else 0
    numbers[last_spoken] = i

print(last_spoken)
