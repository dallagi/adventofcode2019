import unittest
from orbits import build_planets_tree, total_number_of_orbits, minimum_number_of_orbital_transfers

class TestTotalNumberOfOrbits(unittest.TestCase):
    def test_total_number_of_orbits(self):
        orbits = ('COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L')
        tree = build_planets_tree(orbits, 'COM')

        self.assertEqual(total_number_of_orbits(tree, orbits), 42)

    def test_minimum_number_of_orbital_transfers(self):
        orbits = ("COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN")
        tree = build_planets_tree(orbits, 'COM')

        self.assertEqual(minimum_number_of_orbital_transfers(tree, orbits, 'YOU', 'SAN'), 4)

if __name__ == '__main__':
    unittest.main()
