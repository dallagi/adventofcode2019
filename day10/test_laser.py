import textwrap
import unittest

from monitoring_station import seen_asteroids_count, asteroids_from, aligned, best_position, relative_coordinates, polar_coordinates
from laser import find_nth_destroyed, cartesian_coordinates, absolute_coordinates

class TestLaser(unittest.TestCase):
    def test_conversions(self):
        center = (1, 1)
        point = (2, 3)
        new_point = absolute_coordinates(
                cartesian_coordinates(
                    polar_coordinates(
                        relative_coordinates(point, center)
                    )), center)
        self.assertEqual(point, new_point)

    def test_laser(self):
        asteroids_map = textwrap.dedent("""
                .#..##.###...#######
                ##.############..##.
                .#.######.########.#
                .###.#######.####.#.
                #####.##.#.##.###.##
                ..#####..#.#########
                ####################
                #.####....###.#.#.##
                ##.#################
                #####.##.###..####..
                ..######..##.#######
                ####.##.####...##..#
                .#####..#.######.###
                ##...#.##########...
                #.##########.#######
                .####.#.###.###.#.##
                ....##.##.###..#####
                .#.#.###########.###
                #.#.#.#####.####.###
                ###.##.####.##.#..##
        """)
        asteroids = asteroids_from(asteroids_map)
        self.assertEqual(find_nth_destroyed(1, asteroids), (11, 12))
        self.assertEqual(find_nth_destroyed(10, asteroids), (12, 8))
        self.assertEqual(find_nth_destroyed(50, asteroids), (16, 9))
        self.assertEqual(find_nth_destroyed(100, asteroids), (10, 16))
        self.assertEqual(find_nth_destroyed(200, asteroids), (8, 2))
        self.assertEqual(find_nth_destroyed(299, asteroids), (11, 1))

if __name__ == '__main__':
    unittest.main(verbosity=3, buffer=True)

