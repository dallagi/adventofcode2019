
class IntCodeVM:
    EXIT_OPCODE = 99

    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def run(self):
        while(self.instruction() != self.EXIT_OPCODE):
            self.execute(self.instruction())
        return self.numbers

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
        instruction_code = self.numbers[self.index]
        return int(str(instruction_code).zfill(2)[-2:])

    def parameters(self, count):
        params = self.numbers[self.index+1:self.index+count+1]
        res = [ self.get_param(param, mode) 
                for param, mode in zip(params, self.parameter_modes(count)) ]
        return res

    def get_param(self, param, mode):
        if mode == 1:
            return param
        return self.numbers[param]

    def parameter_modes(self, count):
        instruction_code = self.numbers[self.index]
        return [int(mode) for mode in str(instruction_code)[:-2].zfill(count)[::-1]]

    def _op_add(self):
        a, b = self.parameters(2)
        result = self.numbers[self.index + 3]
        
        self.numbers[result] = a + b
        self.index += 4

    def _op_multiply(self):
        a, b = self.parameters(2)
        result = self.numbers[self.index + 3]
        
        self.numbers[result] = a * b
        self.index += 4

    def _op_input(self):
        result = self.numbers[self.index + 1]
        given_input = int(input("> "))
        self.numbers[result] = given_input
        self.index += 2

    def _op_output(self):
        value, = self.parameters(1)
        print(value)
        self.index += 2

    def _op_conditional_jump(self, condition):
        value, position = self.parameters(2)
        if condition(value):
            self.index = position
        else:
            self.index += 3

    def _op_compare(self, comparison):
        a, b = self.parameters(2)
        result_idx = self.numbers[self.index + 3]
        self.numbers[result_idx] = int(comparison(a, b))

        self.index += 4

def read_input():
    return [int(n) for n in open('input').read().split(',')]

if __name__ == '__main__':
    print(IntCodeVM(read_input()).run())

