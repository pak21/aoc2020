#!/usr/bin/env python3

import sys

def parse_line(l):
    return list(filter(lambda c: c != ' ', l))

with open(sys.argv[1]) as f:
    expressions = list(map(lambda l: parse_line(l.strip()), f.readlines()))

def evaluate_expression(it):
    last_op = None
    result = 0
    while True:
        c = next(it, None)
        if not c:
            return result
        if c == '(':
            v = evaluate_expression(it) 
        elif c == ')':
            return result
        elif c == '+':
            last_op = '+'
            continue
        elif c == '*':
            last_op = '*'
            continue
        else:
            v = int(c)

        if not last_op:
            result = v
        elif last_op == '+':
            result = result + v
        elif last_op == '*':
            result = result * v

print(sum(map(lambda e: evaluate_expression(iter(e)), expressions)))
