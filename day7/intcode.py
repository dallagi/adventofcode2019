import asyncio
from itertools import permutations

class IntCodeVM:
    EXIT_OPCODE = 99

    def __init__(self, program, initial_inputs=None):
        self.program = program[::]
        self.index = 0
        self._inputs = initial_inputs
        self.inputs = iter(self._inputs)
        self.outputs = []

    def run(self):
        while not self.finished():
            res = self.execute(self.instruction())

            if res is not None:
                yield res

        yield self.outputs[-1]

    def add_input(self, value):
        self._inputs.append(value)

    def finished(self):
        return self.instruction() == self.EXIT_OPCODE

    def execute(self, instruction):
        if instruction == 1:
            self._op_add()
        if instruction == 2:
            self._op_multiply()
        if instruction == 3:
            self._op_input()
        if instruction == 4:
            return self._op_output()
        if instruction == 5:
            self._op_conditional_jump(lambda x: x)
        if instruction == 6:
            self._op_conditional_jump(lambda x: not x)
        if instruction == 7:
            self._op_compare(lambda a, b: a < b)
        if instruction == 8:
            self._op_compare(lambda a, b: a == b)

    def instruction(self):
        instruction_code = self.program[self.index]
        return int(str(instruction_code).zfill(2)[-2:])

    def parameters(self, count):
        params = self.program[self.index+1:self.index+count+1]
        res = [ self._get_param(param, mode) 
                for param, mode in zip(params, self._parameter_modes(count)) ]
        return res

    def _get_param(self, param, mode):
        if mode == 1:
            return param
        return self.program[param]

    def _parameter_modes(self, count):
        instruction_code = self.program[self.index]
        return [int(mode) for mode in str(instruction_code)[:-2].zfill(count)[::-1]]

    def _op_add(self):
        a, b = self.parameters(2)
        result_idx = self.program[self.index + 3]
        
        self.program[result_idx] = a + b
        self.index += 4

    def _op_multiply(self):
        a, b = self.parameters(2)
        result_idx = self.program[self.index + 3]
        
        self.program[result_idx] = a * b
        self.index += 4

    def _op_input(self):
        result_idx = self.program[self.index + 1]
        given_input = int(input('> ')) if self.inputs is None else next(self.inputs)
        self.program[result_idx] = given_input
        self.index += 2

    def _op_output(self):
        value, = self.parameters(1)
        self.index += 2
        self.outputs.append(value)
        return value

    def _op_conditional_jump(self, condition):
        value, position = self.parameters(2)
        if condition(value):
            self.index = position
        else:
            self.index += 3

    def _op_compare(self, comparison):
        a, b = self.parameters(2)
        result_idx = self.program[self.index + 3]
        self.program[result_idx] = int(comparison(a, b))

        self.index += 4


class IntCodeVMsChain:
    INITIAL_INPUT = 0

    def __init__(self, program, phases):
        self.program = program
        self.phases = phases

    def run(self):
        last_output = [self.INITIAL_INPUT]
        for phase in self.phases:
            last_output = list(IntCodeVM(self.program, [phase] + last_output).run())
        return last_output[-1]

class IntCodeVMsChainWithFeedback:
    INITIAL_INPUT = 0

    def __init__(self, program, phases):
        self.program = program
        self.phases = phases

    def run(self):
        last_output = [self.INITIAL_INPUT]
        machines = [ IntCodeVM(self.program, [phase]) for phase in self.phases ]

        machines[0].add_input(0)
        idx = 0
        while True:
            machine = machines[idx % len(machines)]
            output = next(machine.run())
            is_last = (idx % len(machines)) == (len(machines) - 1)
            if is_last and machine.finished():
                return output
            machines[(idx + 1) % len(machines)].add_input(output)
            idx += 1

        return last_output


def find_maximum_signal(program):
    best = 0

    for phases in permutations(range(5), 5):
        res = IntCodeVMsChain(program, phases).run()
        if int(res) > best:
            best = res
    return best

def find_maximum_signal_with_feedback_loop(program):
    best = 0

    for phases in permutations(range(5, 10), 5):
        res = IntCodeVMsChainWithFeedback(program, phases).run()
        if int(res) > best:
            best = res
    return best


def read_input():
    return [int(n) for n in open('input').read().split(',')]

if __name__ == '__main__':
    print("Highest signal that can be sent to the thrusters: ", find_maximum_signal(read_input()))
    print("Highest signal that can be sent to the thrusters using feedback loop: ", find_maximum_signal_with_feedback_loop(read_input()))
    
