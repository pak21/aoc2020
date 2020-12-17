#!/usr/bin/env python3

import sys

import pandas as pd

def parse_line(l):
    return list(map(int, (l[0:2], l[4:10], l[12:16])))

with open(sys.argv[1]) as f:
    lines = map(parse_line, f.readlines())

df = pd.DataFrame(lines, columns=['day', 'gold', 'silver']).set_index('day')
df['ratio'] = df['silver'] / (df['silver'] + df['gold'])
print(df.sort_values('ratio', ascending=False))
