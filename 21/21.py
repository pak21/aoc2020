#!/usr/bin/env python3

import itertools
import operator
import re
import sys

def parse_line(l):
    match = re.fullmatch(r'(.*) \(contains (.*)\)', l.strip())
    i_text, a_text = match.groups()
    return {'ing': set(i_text.split(' ')), 'alleg': set(a_text.split(', '))}

with open(sys.argv[1]) as f:
    foods = list(map(parse_line, f.readlines()))

all_ing = set.union(*map(lambda f: f['ing'], foods))
all_alleg = set.union(*map(lambda f: f['alleg'], foods))

safe_ing = set()
part1_count = 0

for ing in all_ing:
    invalid_alleg = set()
    for alleg in all_alleg:
        for food in foods:
            if alleg in food['alleg'] and ing not in food['ing']:
                invalid_alleg.add(alleg)

    if len(invalid_alleg) == len(all_alleg):
        safe_ing.add(ing)
        part1_count += len(list(filter(lambda f: ing in f['ing'], foods)))

print(part1_count)

for possible in itertools.permutations(all_ing - safe_ing):
    hypothesis = list(zip(all_alleg, possible))
    bad = any(filter(lambda f: any(filter(lambda p: p[0] in f['alleg'] and p[1] not in f['ing'], hypothesis)), foods))

    if not bad:
        print(','.join(map(lambda p: p[1],sorted(hypothesis))))
