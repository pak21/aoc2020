#!/usr/bin/env python3

import sys

def combine(fn, answers):
   return sum(map(lambda s: len(fn(s)), answers))

with open(sys.argv[1]) as f:
    text = f.read().strip()

answers = list(map(lambda g: list(map(set, g.split('\n'))), text.split('\n\n')))
print(combine(lambda sets: set.union(*sets), answers))
print(combine(lambda sets: set.intersection(*sets), answers))
