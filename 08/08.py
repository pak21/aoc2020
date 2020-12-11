#!/usr/bin/env python3

import sys

import aocvm

with open(sys.argv[1]) as f:
    instructions = aocvm.read_program(f)

old_state, new_state = aocvm.run_program(instructions)
print('With no modifications, entered a loop with the accumulator at {}'.format(old_state.acc))

for to_modify in range(len(instructions)):
    if instructions[to_modify].opcode == 'acc':
        continue

    old_instruction = instructions[to_modify]
    instructions[to_modify] = aocvm.Instruction('nop' if instructions[to_modify].opcode == 'jmp' else 'jmp', instructions[to_modify].arg)
    old_state, new_state = aocvm.run_program(instructions)
    if new_state.pc == len(instructions):
        print('After modifying instruction {}, final value of the accumulator was {}'.format(to_modify, old_state.acc))
    instructions[to_modify] = old_instruction
