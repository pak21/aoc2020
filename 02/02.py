#!/usr/bin/env python3

import re
import sys

RULE_RE = r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$'

with open(sys.argv[1]) as f:
    rules_text = f.readlines()

def extract(rule_text):
    match = re.match(RULE_RE, rule_text)
    groups = match.groups()
    return (int(groups[0]), int(groups[1]), *groups[2:])

def valid(rule):
    count_min, count_max, character, password = rule
    character_count = len(password) - len(password.replace(character, ''))
    return character_count >= count_min and character_count <= count_max

def valid2(rule):
    pos1, pos2, character, password = rule
    return (password[pos1-1] == character) != (password[pos2-1] == character)

rules = [extract(text) for text in rules_text]
is_valid = [valid(rule) for rule in rules]

print(sum(is_valid))
print(sum(is_valid2))
