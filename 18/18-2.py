#!/usr/bin/env python3

import sys

def parse_line(l):
    return list(filter(lambda c: c != ' ', l))

with open(sys.argv[1]) as f:
    expressions = list(map(lambda l: parse_line(l.strip()), f.readlines()))

def evaluate_simple(tokens):
    try:
        while True:
            i = tokens.index('+')
            tokens = tokens[:i-1] + [tokens[i-1] + tokens[i+1]] + tokens[i+2:]
    except ValueError:
        pass

    try:
        while True:
            i = tokens.index('*')
            tokens = tokens[:i-1] + [tokens[i-1] * tokens[i+1]] + tokens[i+2:]
    except ValueError:
        pass

    return tokens[0]

def evaluate_expression(it):
    foo = []
    while True:
        c = next(it, None)
        if not c or c == ')':
            bar = evaluate_simple(foo)
            return bar
        elif c == '(':
            foo.append(evaluate_expression(it))
        elif c == '+' or c == '*':
            foo.append(c)
        else:
            foo.append(int(c))

print(sum(map(lambda e: evaluate_expression(iter(e)), expressions)))
