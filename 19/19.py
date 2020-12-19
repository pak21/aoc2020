#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as f:
    rules_text, examples_text = f.read().strip().split('\n\n')

rules = dict(map(lambda l: l.split(': '), rules_text.split('\n')))
examples = list(examples_text.split())

def build_regexp(rule_text, rules):
    if rule_text == '"a"' or rule_text == '"b"':
        return rule_text[1]
    elif '|' in rule_text:
        subrules = map(lambda rt: build_regexp(rt, rules), rule_text.split(' | '))
        return "{}|{}".format(*subrules)
    else:
        subrules = map(lambda r: '(' + build_regexp(rules[r], rules) + ')', rule_text.split(' '))
        return '(' + ''.join(subrules) + ')'

# Part 1

rule0 = re.compile('^' + build_regexp(rules['0'], rules) + '$')
print(sum(map(lambda e: re.match(rule0, e) != None, examples)))

# Part 2

MAX_REPEATS = 10

def build_rule0(rule31, rule42, repeats):
    rule8 = '(' + rule42 + ')+'
    rule42s = ''.join([rule42] * repeats)
    rule31s = ''.join([rule31] * repeats)
    rule11 = '(' + rule42s + rule31s + ')'
    return re.compile('^({})({})$'.format(rule8, rule11))
    
rule31 = '(' + build_regexp(rules['31'], rules) + ')'
rule42 = '(' + build_regexp(rules['42'], rules) + ')'
rule0s = [None] + list(map(lambda i: build_rule0(rule31, rule42, i), range(1, MAX_REPEATS)))

def try_matches(example):
    for i in range(1, MAX_REPEATS):
        match = re.match(rule0s[i], example)
        if match:
            return True
    return False

print(sum(map(lambda e: try_matches(e), examples)))
