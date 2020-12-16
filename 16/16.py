#!/usr/bin/env python3

import math
import re
import sys

import numpy as np

with open(sys.argv[1]) as f:
    fields_text, ticket_text, nearby_text = f.read().strip().split('\n\n')

def parse_field(l):
    match = re.match(r'^(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$', l)
    groups = list(match.groups())
    return (groups[0], list(map(int, groups[1:])))

fields = list(map(parse_field, fields_text.split('\n')))

def parse_ticket(l):
    return list(map(int, l.split(',')))

ticket = parse_ticket(ticket_text.split('\n')[1])

nearby = list(map(parse_ticket, nearby_text.split('\n')[1:]))

# Part 1

def is_valid_field(field, value):
    limits = field[1]
    return (value >= limits[0] and value <= limits[1]) or (value >= limits[2] and value <= limits[3])

error_rate = 0
for nearby_ticket in nearby:
    for field_value in nearby_ticket:
        valid = any(map(lambda f: is_valid_field(f, field_value), fields))
        if not valid:
            error_rate += field_value

print(error_rate)

# Part 2

valid_tickets = np.array(list(filter(lambda nt: all(map(lambda field_value: any(map(lambda f: is_valid_field(f, field_value), fields)), nt)), nearby)))

field_validity = []
for i in range(len(fields)):
    row = []
    field_validity.append(row)
    field = fields[i]
    for j in range(len(fields)):
        column = valid_tickets[:,j]
        valid = all(list(map(lambda v: is_valid_field(field, v), column)))
        row.append(valid)

field_validity_np = np.array(field_validity)

mapping = [-1] * len(fields)
while True:
    sums = np.sum(field_validity_np, axis=1)
    unique_matches = np.where(sums == 1)
    if len(unique_matches[0]) == 0:
        break
    unique_match = unique_matches[0][0]
    column = np.where(field_validity_np[unique_match])[0][0]
    print('Field {} ({}) is column {}'.format(unique_match, fields[unique_match][0], column))
    mapping[unique_match] = column

    field_validity_np[:,column] = False

print(math.prod(map(lambda f: ticket[mapping[f]], map(lambda p: p[0], filter(lambda p: p[1][0].startswith('departure'), enumerate(fields))))))
