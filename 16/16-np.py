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

nearby = np.array(list(map(parse_ticket, nearby_text.split('\n')[1:])))

# Part 1

def is_valid_field(field, value):
    limits = field[1]
    return (value >= limits[0] and value <= limits[1]) or (value >= limits[2] and value <= limits[3])

# 3D array containing whether a particular (field, ticket, column) is valid
field_validity = np.array(list(map(lambda f: np.vectorize(lambda v: is_valid_field(f, v))(nearby), fields)))

# 2D array containing whether a particular (ticket, column) has any valid fields
any_field_validity = np.any(field_validity, axis=0)

## Part 1: the sum of all values which cannot possibly be a valid field
print(np.sum(np.logical_not(any_field_validity) * nearby))

## Part 2

# We want only tickets where all fields are valid
is_ticket_valid = np.all(any_field_validity, axis=1)

# 2D array containing whether a particular (field, column) is valid for all valid tickets
field_column_validity = np.all(field_validity[:,is_ticket_valid,:], axis=1)

# How many possibile column assignments there are for each field
# The structure of the problem is set so that this contains one entry each of (1, 2, ..., #fields)
counts = np.sum(field_column_validity, axis=1)

# Taking the set of possible assignments, we can work out the order to assign columns to fields
field_assignment_order = list(map(lambda p: p[1], sorted(map(lambda p: (p[1], p[0]), enumerate(counts)))))

# Our final mapping of fields to columns
field_mapping = [None] * field_column_validity.shape[0]

# Whether each column is still available for assignment
column_available = [True] * field_column_validity.shape[1]

for field in field_assignment_order:
    # Find the column which is valid for this field and hasn't already been assigned
    next_column = np.argmax(field_column_validity[field] * column_available)

    # Note the mapping for this field and that this column is unavailable for future assignments
    field_mapping[field] = next_column
    column_available[next_column] = False

# And finally a tedious bit of processing to get the answer
# Could have cheated slightly here because the "departure" fields are the first 6 in my list anyway
print(math.prod(map(lambda f: ticket[field_mapping[f]], map(lambda p: p[0], filter(lambda p: p[1][0].startswith('departure'), enumerate(fields))))))
