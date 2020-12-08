#!/usr/bin/env python3

import sys

OPCODE_FNS = {
    'acc': lambda s, a: (s[0] + 1, s[1] + a),
    'jmp': lambda s, a: (s[0] + a, s[1]),
    'nop': lambda s, a: (s[0] + 1, s[1])
}

with open(sys.argv[1]) as f:
    text = f.read().strip()

def parse_line(line):
    opcode, value = line.split(' ')
    return opcode, int(value)

lines = text.split('\n')
opcodes = list(map(parse_line, lines))

def run_program():
    state = (0, 0)
    visited = {0}

    while True:
        visited.add(state[0])
        next_opcode = opcodes[state[0]]
        next_fn = OPCODE_FNS[next_opcode[0]]

        next_state = next_fn(state, next_opcode[1])
        if next_state[0] in visited or next_state[0] >= len(opcodes):
            return state, next_state

        state = next_state

    return state

final_state = run_program()
print(final_state[0][1])

for to_modify in range(len(opcodes)):
    if opcodes[to_modify][0] == 'acc':
        continue

    opcodes[to_modify] = ('nop' if opcodes[to_modify][0] == 'jmp' else 'jmp', opcodes[to_modify][1])
    final_state = run_program()
    if final_state[1][0] == len(opcodes):
        print(to_modify, final_state[0][1])
    opcodes[to_modify] = ('nop' if opcodes[to_modify][0] == 'jmp' else 'jmp', opcodes[to_modify][1])
