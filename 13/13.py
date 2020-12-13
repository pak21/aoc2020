#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    earliest = int(f.readline())
    buses = list(map(lambda s: int(s) if s != 'x' else None, f.readline().split(',')))

def part1(earliest, buses):
    time = earliest
    running_buses = list(filter(None, buses))
    while True:
        for bus in running_buses:
            if (time % bus) == 0:
                return bus * (time - earliest)
        time = time + 1

print(part1(earliest, buses))

matches = list(filter(lambda p: p[1], enumerate(buses)))

time = 0
factor = 1
for offset, period in matches:
    target = (period - offset) % period
    while time % period != target:
        time += factor
    factor *= period
print(time)
