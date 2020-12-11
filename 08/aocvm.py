class VmState:
    def __init__(self, pc, acc):
        self.pc = pc
        self.acc = acc

_OPCODE_FNS = {
    'acc': lambda s, a: VmState(s.pc + 1, s.acc + a),
    'jmp': lambda s, a: VmState(s.pc + a, s.acc),
    'nop': lambda s, a: VmState(s.pc + 1, s.acc)
}

class Instruction:
    def __init__(self, opcode, arg):
        self.opcode = opcode
        self.arg = arg
        
        self._fn = _OPCODE_FNS[opcode]

def _parse_instruction(line):
    opcode, value = line.split(' ')
    return Instruction(opcode, int(value))

def read_program(f):
    return list(map(_parse_instruction, f.readlines()))

def run_program(instructions):
    state = VmState(0, 0)
    visited = set()

    while True:
        visited.add(state.pc)
        instruction = instructions[state.pc]
        next_state = instruction._fn(state, instruction.arg)
        if next_state.pc in visited or next_state.pc >= len(instructions):
            return state, next_state

        state = next_state
