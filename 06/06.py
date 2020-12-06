#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    text = f.read().strip()

groups = text.split('\n\n')
print(sum(map(lambda g: len(set(g.replace('\n', ''))), groups)))
print(sum(map(lambda g: len(set.intersection(*map(lambda s: set(s), g.split('\n')))), groups)))
