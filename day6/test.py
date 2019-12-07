import unittest
from orbits import PlanetsTree

class TestPlanetTree(unittest.TestCase):
    def test_total_number_of_orbits(self):
        orbits = ('COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L')
        tree = PlanetsTree.from_orbits(orbits)

        self.assertEqual(tree.total_number_of_orbits(), 42)

    def test_minimum_number_of_orbital_transfers(self):
        orbits = ("COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN")
        tree = PlanetsTree.from_orbits(orbits)

        self.assertEqual(tree.minimum_number_of_orbital_transfers('YOU', 'SAN'), 4)

if __name__ == '__main__':
    unittest.main()
