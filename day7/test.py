import unittest
from intcode import IntCodeVM, IntCodeVMsChain, find_maximum_signal

class TestPlanetTree(unittest.TestCase):
    def test_intcode(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        
        self.assertEqual(IntCodeVM(program, [7]).run(), [999])
        self.assertEqual(IntCodeVM(program, [8]).run(), [1000])
        self.assertEqual(IntCodeVM(program, [9]).run(), [1001])

    def test_intcode_chain(self):
        program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        phases = [4, 3, 2, 1, 0]

        self.assertEqual(IntCodeVMsChain(program, phases).run(), [43210])

    def test_find_maximum_signal(self):
        program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

        self.assertEqual(find_maximum_signal(program), 65210)

if __name__ == '__main__':
    unittest.main()
