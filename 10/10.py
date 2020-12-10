#!/usr/bin/env python3

import collections
import math
import sys

with open(sys.argv[1]) as f:
    input_text = f.read().strip()

without_ends = sorted(map(int, input_text.split()))
adapters = [0] + without_ends + [without_ends[-1] + 3]
diffs = list(map(lambda p: p[1] - p[0], zip(adapters, adapters[1:])))

counts = collections.Counter(diffs)
print(counts[1] * counts[3])

def rle(seq):
    run = 0
    for x in seq:
        if x == 3:
            yield run
            run = 0
        else:
            run = run + 1

runs_to_combinations = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}

combinations = map(lambda r: runs_to_combinations[r], rle(diffs))
print(math.prod(combinations))
