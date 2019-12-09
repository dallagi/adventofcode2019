import unittest
from intcode import IntCodeVM, IntCodeVMsChain, IntCodeVMsChainWithFeedback, find_maximum_signal, find_maximum_signal_with_feedback_loop

class TestPlanetTree(unittest.TestCase):
    def test_intcode(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        
        self.assertEqual(list(IntCodeVM(program, [7]).run())[0], 999)
        self.assertEqual(list(IntCodeVM(program, [8]).run())[0], 1000)
        self.assertEqual(list(IntCodeVM(program, [9]).run())[0], 1001)

    def test_intcode_chain(self):
        program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        phases = [4, 3, 2, 1, 0]

        self.assertEqual(IntCodeVMsChain(program, phases).run(), 43210)

    def test_find_maximum_signal(self):
        program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

        self.assertEqual(find_maximum_signal(program), 65210)

    def test_feedback_loop(self):
        program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        phases = [9,8,7,6,5]

        self.assertEqual(IntCodeVMsChainWithFeedback(program, phases).run(), 139629729)

    def test_find_maximum_signal_with_feedback_loop(self):
        program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

        self.assertEqual(find_maximum_signal_with_feedback_loop(program), 139629729)

if __name__ == '__main__':
    unittest.main()
