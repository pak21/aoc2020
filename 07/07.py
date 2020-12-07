#!/usr/bin/env python3

import collections
import re
import sys

with open(sys.argv[1]) as f:
    text = f.read().strip()

def parse_inner(text):
    match = re.search('^([0-9+]) (.*) bags?$', text)
    return int(match.group(1)), match.group(2)

def parse_rule(outer, inner_text):
    inner = [] if inner_text == 'no other bags' else list(map(lambda t: parse_inner(t), inner_text.split(', ')))
    return outer, inner

rules = dict(map(lambda t: parse_rule(*t.strip('.').split(' bags contain ')), text.split('\n')))

inverted = collections.defaultdict(collections.deque)
for parent, children in rules.items():
    for child in children:
        inverted[child[1]].append(parent)

todo = collections.deque(['shiny gold'])
seen = set()
while todo:
   inner = todo.popleft()
   todo = todo + inverted[inner]
   seen.add(inner)

print(len(seen) - 1)

def recurse(colour):
    return 1 + sum(map(lambda rule: rule[0] * recurse(rule[1]), rules[colour]))

print(recurse('shiny gold') - 1)
