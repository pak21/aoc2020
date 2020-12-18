#!/usr/bin/env python3

import sys


with open(sys.argv[1]) as f:
    expressions = f.readlines()

PART1_PRIORITIES = {'+': 0, '*': 0}
PART2_PRIORITIES = {'+': 1, '*': 0}

REDUCERS = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b
}

def reduce_operator(value_stack, operator_stack):
    a = value_stack[-2]
    b = value_stack[-1]
    o = operator_stack[-1]
    v = REDUCERS[o](a, b)
    return value_stack[:-2] + [v], operator_stack[:-1]

def evaluate_simple(tokens, priorities):
    value_stack = []
    operator_stack = []

    for t in tokens:
        if t == '+' or t == '*':
            if operator_stack and priorities[t] <= priorities[operator_stack[-1]]:
                value_stack, operator_stack = reduce_operator(value_stack, operator_stack)
            operator_stack.append(t)
        else:
            value_stack.append(t)

    while operator_stack:
        value_stack, operator_stack = reduce_operator(value_stack, operator_stack)

    return value_stack[0]

def evaluate_expression(it, priorities):
    tokens = []
    while True:
        c = next(it)
        if c == '\n' or c == ')':
            return evaluate_simple(tokens, priorities)
        elif c == ' ':
            pass
        elif c == '(':
            tokens.append(evaluate_expression(it, priorities))
        elif c == '+' or c == '*':
            tokens.append(c)
        else:
            tokens.append(int(c))

print(sum(map(lambda e: evaluate_expression(iter(e), PART1_PRIORITIES), expressions)))
print(sum(map(lambda e: evaluate_expression(iter(e), PART2_PRIORITIES), expressions)))
