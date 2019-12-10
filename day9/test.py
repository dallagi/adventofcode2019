import unittest
from intcode import IntCodeVM

class TestIntCodeVm(unittest.TestCase):
    def test_first_given_example(self):
        program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

        self.assertEqual(list(IntCodeVM(program, [1]).run())[0], 109)

    def test_second_given_example(self):
        program = [104,1125899906842624,99]
        
        self.assertEqual(list(IntCodeVM(program, [1]).run())[0], 1125899906842624)

    def test_third_given_example(self):
        program = [1102,34915192,34915192,7,4,7,99,0]

        self.assertEqual(list(IntCodeVM(program, [1]).run())[0], 1219070632396864)


if __name__ == '__main__':
    unittest.main()
