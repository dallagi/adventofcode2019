import unittest

from arcade import Arcade

def flatten(l):
    return [item for sublist in l for item in sublist]

def intcode_program_to_output(digits):
    return flatten([104, digit] for digit in digits) + [99]

class TestArcade(unittest.TestCase):
    def test_block_tiles_count(self):
        BLOCK_TILE = 2
        program = intcode_program_to_output([1,2,3,6,5,BLOCK_TILE])

        arcade = Arcade(program)
        arcade.run()

        self.assertEqual(arcade.grid.count_of_tiles_of_type(BLOCK_TILE), 1)

    def test_show_score(self):
        program = intcode_program_to_output([-1,0,12345])

        arcade = Arcade(program)
        arcade.run()

        self.assertEqual(arcade.score, 12345)

if __name__ == '__main__':
    unittest.main(verbosity=3)

