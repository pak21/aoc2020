#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as f:
    rules_text, examples_text = f.read().strip().split('\n\n')

def parse_rule(l):
    return l.split(': ')

rules = dict(map(parse_rule, rules_text.split('\n')))
examples = list(examples_text.split())

def build_regexp(rule_text, rules):
    if rule_text == '"a"' or rule_text == '"b"':
        return rule_text[1]
    elif '|' in rule_text:
        left, right = rule_text.split(' | ')
        subrules = list(map(lambda rt: '(' + build_regexp(rt, rules) + ')', [left, right]))
        return "({})|({})".format(*subrules)
    else:
        subrules = list(map(lambda r: '(' + build_regexp(rules[r], rules) + ')', rule_text.split(' ')))
        return '(' + ''.join(subrules) + ')'

# Part 1

rule0_text = '^' + build_regexp(rules['0'], rules) + '$'
rule0 = re.compile(rule0_text)

print(sum(map(lambda e: re.match(rule0, e) != None, examples)))

# Part 2

rule31 = '(' + build_regexp(rules['31'], rules) + ')'
rule42 = '(' + build_regexp(rules['42'], rules) + ')'

rule8 = '(' + rule42 + ')+'

def try_matches(example):
    for i in range(1, 10):
        rule42s = ''.join([rule42] * i)
        rule31s = ''.join([rule31] * i)
        rule11 = '(' + rule42s + rule31s + ')'
        new_rule0_text = '^({})({})$'.format(rule8, rule11)
        match = re.match(new_rule0_text, example)
        if match:
            return True
    return False

print(sum(map(lambda e: try_matches(e), examples)))
