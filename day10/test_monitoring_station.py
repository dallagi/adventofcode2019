import textwrap
import unittest

from monitoring_station import seen_asteroids_count, asteroids_from, aligned, best_position

class TestMonitoringStation(unittest.TestCase):
    def test_asteroids_map(self):
        asteroids_map = textwrap.dedent("""
                ..#
                #.#
                ...
                """)

        self.assertEqual(asteroids_from(asteroids_map), [(2,0), (0, 1), (2,1)])

    def test_number_of_asteroids_seen(self):
        asteroids_map = textwrap.dedent("""
            ......#.#.
            #..#.#....
            ..#######.
            .#.#.###..
            .#..#.....
            ..#....#.#
            #..#....#.
            .##.#..###
            ##...#..#.
            .#....####
        """)
        self.assertEqual(seen_asteroids_count(asteroids_from(asteroids_map), (5, 8)), 33)

    def test_best_location(self):
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
        self.assertEqual(best_position(asteroids), (11, 13))
        self.assertEqual(seen_asteroids_count(asteroids, (11, 13)), 210)

    def test_given_example(self):
        asteroids_map = textwrap.dedent("""
                .#..#..###
                ####.###.#
                ....###.#.
                ..###.##.#
                ##.##.#.#.
                ....###..#
                ..#.#..#.#
                #..#.#.###
                .##...##.#
                .....#.#..
        """)
        asteroids = asteroids_from(asteroids_map)
        self.assertEqual(best_position(asteroids), (6, 3))
        self.assertEqual(seen_asteroids_count(asteroids, (6, 3)), 41)

    def test_another_given_example(self):
        asteroids_map = textwrap.dedent("""
                #.#...#.#.
                .###....#.
                .#....#...
                ##.#.#.#.#
                ....#.#.#.
                .##..###.#
                ..#...##..
                ..##....##
                ......#...
                .####.###.
        """)
        asteroids = asteroids_from(asteroids_map)
        self.assertEqual(best_position(asteroids), (1, 2))
        self.assertEqual(seen_asteroids_count(asteroids, (1, 2)), 35)

if __name__ == '__main__':
    unittest.main(verbosity=3, buffer=True)

