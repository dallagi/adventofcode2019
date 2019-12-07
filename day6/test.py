import unittest
from orbits import build_planets_tree, total_number_of_orbits

class TestTotalNumberOfOrbits(unittest.TestCase):
    def test_provided_example(self):
        orbits = ('COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L')
        tree = build_planets_tree(orbits, 'COM')

        self.assertEqual(total_number_of_orbits(tree, orbits), 42)

if __name__ == '__main__':
    unittest.main()
