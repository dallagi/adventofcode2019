
class IntCodeVM:
    EXIT_OPCODE = 99

    def __init__(self, program, inputs=None):
        self.program = program[::]
        self.index = 0
        self.inputs = iter(inputs)
        self.outputs = []

    def run(self):
        while(self.instruction() != self.EXIT_OPCODE):
            self.execute(self.instruction())
        return self.outputs

    def execute(self, instruction):
        if instruction == 1:
            self._op_add()
        elif instruction == 2:
            self._op_multiply()
        elif instruction == 3:
            self._op_input()
        elif instruction == 4:
            self._op_output()
        elif instruction == 5:
            self._op_conditional_jump(lambda x: x)
        elif instruction == 6:
            self._op_conditional_jump(lambda x: not x)
        elif instruction == 7:
            self._op_compare(lambda a, b: a < b)
        elif instruction == 8:
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
        self.outputs.append(value)
        self.index += 2

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
            last_output = IntCodeVM(self.program, [phase] + last_output).run()
        return last_output


def find_maximum_signal(program):
    best = 0
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        phases = (a, b, c, d, e)
                        if len(set(phases)) < 5:
                            continue

                        res = IntCodeVMsChain(program, phases).run()
                        if int(res[0]) > best:
                            best = res[0]
    return best


def read_input():
    return [int(n) for n in open('input').read().split(',')]

if __name__ == '__main__':
    print("Highest signal that can be sent to the thrusters: ", find_maximum_signal(read_input()))
    
