#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    values = sorted([int(l) for l in f.readlines()])

for i in range(0, len(values)):
    v1 = values[i]
    for v2 in values[i+1:]:
        s = v1 + v2
        if s == 2020:
            print(v1, v2, s, v1 * v2)
        if s > 2020:
            break

for i in range(0, len(values)):
    v1 = values[i]
    for j in range(i+1, len(values)):
        v2 = values[j]
        if v1 + v2 > 2020:
            break
        for v3 in values[j+1:]:
            s = v1 + v2 + v3
            if s == 2020:
                print(v1, v2, v3, s, v1 * v2 * v3)
            if s > 2020:
                break
