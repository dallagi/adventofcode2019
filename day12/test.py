import unittest

from moons import Moons, Moon

class TestMoons(unittest.TestCase):
    def test_moons_after_one_step(self):
        moon1 = Moon([-1, 0, 2])
        moon2 = Moon([2, -10, -7])
        moon3 = Moon([4, -8, 8])
        moon4 = Moon([3, 5, -1])

        moons = Moons(moon1, moon2, moon3, moon4)
        moons.run_simulation(steps=1)

        m1, m2, m3, m4 = moons.moons
        self.assertEqual(m1.position, [2, -1,  1])
        self.assertEqual(m1.velocity, [3, -1, -1])

        self.assertEqual(m2.position, [3, -7, -4])
        self.assertEqual(m2.velocity, [1,  3,  3])

        self.assertEqual(m3.position, [1, -7,  5])
        self.assertEqual(m3.velocity, [-3, 1, -3])

        self.assertEqual(m4.position, [2,  2,  0])
        self.assertEqual(m4.velocity, [-1, -3, 1])

    def test_moons_after_two_steps(self):
        moon1 = Moon([-1, 0, 2])
        moon2 = Moon([2, -10, -7])
        moon3 = Moon([4, -8, 8])
        moon4 = Moon([3, 5, -1])

        moons = Moons(moon1, moon2, moon3, moon4)
        moons.run_simulation(steps=2)

        m1, m2, m3, m4 = moons.moons
        self.assertEqual(m1.position, [5, -3, -1])
        self.assertEqual(m1.velocity, [3, -2, -2])

        self.assertEqual(m2.position, [1, -2,  2])
        self.assertEqual(m2.velocity, [-2, 5,  6])

        self.assertEqual(m3.position, [1, -4, -1])
        self.assertEqual(m3.velocity, [0,  3, -6])

        self.assertEqual(m4.position, [1, -4,  2])
        self.assertEqual(m4.velocity, [-1, -6, 2])

    def test_moons_after_ten_steps(self):
        moon1 = Moon([-1, 0, 2])
        moon2 = Moon([2, -10, -7])
        moon3 = Moon([4, -8, 8])
        moon4 = Moon([3, 5, -1])

        moons = Moons(moon1, moon2, moon3, moon4)
        moons.run_simulation(steps=10)

        m1, m2, m3, m4 = moons.moons
        self.assertEqual(m1.position, [2, 1, -3])
        self.assertEqual(m1.velocity, [-3, -2, 1])

        self.assertEqual(m2.position, [1, -8, 0])
        self.assertEqual(m2.velocity, [-1, 1, 3])

        self.assertEqual(m3.position, [3, -6, 1])
        self.assertEqual(m3.velocity, [3, 2, -3])

        self.assertEqual(m4.position, [2, 0, 4])
        self.assertEqual(m4.velocity, [1, -1, -1])


    def test_energy(self):
        moon1 = Moon([-1, 0, 2])
        moon2 = Moon([2, -10, -7])
        moon3 = Moon([4, -8, 8])
        moon4 = Moon([3, 5, -1])

        moons = Moons(moon1, moon2, moon3, moon4)
        moons.run_simulation(steps=10)

        self.assertEqual(moons.total_energy(), 179)

    def test_steps_until_repetition(self):
        moon1 = Moon([-1, 0, 2])
        moon2 = Moon([2, -10, -7])
        moon3 = Moon([4, -8, 8])
        moon4 = Moon([3, 5, -1])

        moons = Moons(moon1, moon2, moon3, moon4)
        self.assertEquals(moons.steps_until_repetition(), 2772)

    def test_steps_until_repetition_more_complex(self):
        moons = Moons(
                Moon([-8, -10, 0]),
                Moon([5, 5, 10]),
                Moon([2, -7, 3]),
                Moon([9, -8, -3])
                )

        self.assertEqual(moons.steps_until_repetition(), 4686774924)


if __name__ == '__main__':
    unittest.main(verbosity=3)

