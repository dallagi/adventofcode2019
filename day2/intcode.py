OPERATIONS = {
    1: lambda a, b: a + b,
    2: lambda a, b: a * b
}

EXIT_OPCODE = 99

def execute(numbers):
    index = 0
    while numbers[index] != EXIT_OPCODE:
        op_code = numbers[index]
        numbers = apply_operation(op_code, numbers, index)
        index += 4
    
    return numbers
            
def apply_operation(op_code, numbers, index):
    result_index = numbers[index+3]
    numbers[result_index] = OPERATIONS[op_code](*operation_operands(numbers, index))
    return numbers

def operation_operands(numbers, index):
    operands_indexes = numbers[index+1], numbers[index+2]
    return numbers[operands_indexes[0]], numbers[operands_indexes[1]]

def find_noun_and_verb(input_path, target_output):
    for noun in range(100):
        for verb in range(100):
            numbers = [int(n) for n in open(input_path).read().split(',')]
            numbers[1] = noun
            numbers[2] = verb

            res = execute(numbers)
            if(res[0] == target_output):
                return noun * 100 + verb
    return None

def execute_from_file(path):
    with open(path) as f:
        numbers = [int(n) for n in f.read().split(',')]
        return execute(numbers)

if __name__ == '__main__':
    print(execute_from_file('input'))
    print(find_noun_and_verb('input', 19690720))
