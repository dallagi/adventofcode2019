
class IntCodeVM:
    EXIT_OPCODE = 99
    MAX_PARAMS_COUNT = 3

    def __init__(self, program, initial_inputs=None):
        self.program = self._right_pad(program[::])
        self.index = 0
        self._inputs = initial_inputs or []
        self.inputs = iter(self._inputs)
        self.outputs = []
        self.relative_base = 0

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
        if instruction == 9:
            self._op_adjust_relative_base()

    def instruction(self):
        instruction_code = self.program[self.index]
        return int(str(instruction_code).zfill(2)[-2:])

    def parameters(self, count):
        return [self.parameter(i) for i in range(1, count+1)]

    def parameter(self, offset):
        raw_param = self.program[self.index + offset]
        mode = self._parameter_mode(offset)
        return self._get_param(raw_param, mode)

    def index_for_write(self, offset):
        raw_param = self.program[self.index + offset]
        mode = self._parameter_mode(offset)
        return self._get_index_for_write(raw_param, mode)

    def _get_param(self, param, mode):
        if mode == 1:
            return param
        if mode == 2:
            return self.program[self.relative_base + param]
        return self.program[param]

    def _get_index_for_write(self, param, mode):
        if mode == 2:
            return self.relative_base + param
        return param

    def _parameter_mode(self, offset):
        instruction_code = self.program[self.index]
        return int(str(instruction_code)[:-2].zfill(self.MAX_PARAMS_COUNT)[::-1][offset-1])

    def _right_pad(self, program, pad_size=10000):
        return program + [0] * pad_size

    def _op_add(self):
        a, b = self.parameters(2)
        result_idx = self.index_for_write(3)
        
        self.program[result_idx] = a + b
        self.index += 4

    def _op_multiply(self):
        a, b = self.parameters(2)
        result_idx = self.index_for_write(3)
        
        self.program[result_idx] = a * b
        self.index += 4

    def _op_input(self):
        result_idx = self.index_for_write(1)
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
        result_idx = self.index_for_write(3)
        self.program[result_idx] = int(comparison(a, b))

        self.index += 4

    def _op_adjust_relative_base(self):
        value, = self.parameters(1)
        self.relative_base += value

        self.index += 2


def read_input():
    return [int(n) for n in open('input').read().split(',')]

