#!/usr/bin/env python3

import sys

preamble_length = int(sys.argv[2])

with open(sys.argv[1]) as f:
    ns = list(map(int, f.readlines()))

test_sets = map(lambda i: (ns[i:i+preamble_length], ns[i+preamble_length]), range(len(ns)-preamble_length))

def is_missing(potentials, target):
    return not any(map(lambda i: any(map(lambda b: potentials[i] + b == target, potentials[i+1:])), range(len(potentials))))

part2_target = next(filter(lambda x: is_missing(*x), test_sets))[1]
print(part2_target)

for i in range(len(ns)):
    partial_sum = ns[i]
    for j in range(i+1, len(ns)):
        partial_sum += ns[j]
        if partial_sum == part2_target:
            foo = ns[i:j+1]
            print(min(foo) + max(foo))
        if partial_sum >= part2_target:
            break
