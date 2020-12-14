#!/usr/bin/env python3

import itertools
import re
import sys

def parse_mask(m):
    to_set = 0
    to_clear = 0
    floating = []
    for bit in enumerate(m[::-1]):
        if bit[1] == '1':
            to_set = to_set | (2**bit[0])
        elif bit[1] == '0':
            to_clear = to_clear | (2**bit[0])
        else:
            floating.append(2**bit[0])
    return to_clear, to_set, floating

def parse_instruction(l):
    if l.startswith('mask'):
        return ('mask', parse_mask(l.strip().split(' ')[2]))
    else:
        match = re.match('^mem\[([0-9]+)\] = ([0-9]+)$', l)
        return ('mem', list(map(int, match.groups())))

with open(sys.argv[1]) as f:
    instructions = list(map(parse_instruction, f.readlines()))

current_nask = (0, 0)
current_mem = {}
for instruction in instructions:
    if instruction[0] == 'mask':
        current_mask = instruction[1]
    else:
        value = (instruction[1][1] & ~current_mask[0]) | current_mask[1]
        current_mem[instruction[1][0]] = value

print(sum(current_mem.values()))

def recurse(floating_bits, address, value, mem):
    if floating_bits:
        floating_bit = floating_bits[0]
        remaining = floating_bits[1:]
        recurse(remaining, address & ~floating_bit, value, mem)
        recurse(remaining, address |  floating_bit, value, mem)
    else:
        mem[address] = value

current_mask = (0, 0)
current_mem = {}
for instruction in instructions:
    if instruction[0] == 'mask':
        current_mask = instruction[1]
    else:
        address_to_write = instruction[1][0] | current_mask[1]
        recurse(current_mask[2], address_to_write, instruction[1][1], current_mem)

print(sum(current_mem.values()))
