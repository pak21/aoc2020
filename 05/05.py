#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    ids = set(map(lambda l: sum(map(lambda p: 2**p[0] if p[1] else 0, enumerate(map(lambda c: c == 'B' or c == 'R', l.strip()[::-1])))), f.readlines()))

print(max(ids))
print(list(filter(lambda m: m not in ids, range(min(ids)+1, max(ids)))))
