import copy
import math

from dataclasses import dataclass, field
from functools import reduce
from itertools import combinations, count
from typing import List

@dataclass
class Moon:
    position: List[int]
    velocity: List[int] = field(default_factory = lambda: [0, 0 ,0])

    def __str__(self):
        return f'Moon(position={self.position}, velocity={self.velocity})'

    def apply_velocity(self):
        for axis in range(3):
            self.position[axis] += self.velocity[axis]

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def potential_energy(self):
        return sum(abs(value) for value in self.position)

    def kinetic_energy(self):
        return sum(abs(value) for value in self.velocity)


class Moons:
    def __init__(self, *moons):
        self.moons = moons
        self.initial_moons = tuple(copy.deepcopy(moons))

    def __str__(self):
        return 'Moons\n\t' + '\n\t'.join(str(moon) for moon in self.moons)

    def run_simulation(self, *, steps: int):
        for _ in range(steps):
            self.run_step()

    def run_step(self):
        self._apply_gravity()
        self._apply_velocity()

    def total_energy(self):
        return sum(moon.total_energy() for moon in self.moons)

    def steps_until_repetition(self):
        return self._least_common_multiple(*self.steps_until_first_repetition_by_axis())

    def steps_until_first_repetition_by_axis(self):
        res = [0, 0, 0]

        for step in count():
            for axis_idx, (current_axis_state, initial_axis_state) in enumerate(zip(self.axes_state(), self.initial_axes_state())):
                if current_axis_state == initial_axis_state:
                    res[axis_idx] = res[axis_idx] or step

            if 0 not in res:
                return res
            
            self.run_step()

    def axes_state(self, moons=None):
        if moons is None:
            moons = self.moons
        positions = zip(*[moon.position for moon in moons])
        velocities = zip(*[moon.velocity for moon in moons])
        return zip(positions, velocities)

    def initial_axes_state(self):
        return self.axes_state(self.initial_moons)

    def _apply_gravity(self):
        for moons in combinations(self.moons, 2):
            self._apply_gravity_to_pair(*moons)
    
    def _apply_gravity_to_pair(self, moon1, moon2):
        for axis in range(3):
            value1 = moon1.position[axis]
            value2 = moon2.position[axis]

            if value1 == value2:
                continue
            if value1 > value2:
                moon1.velocity[axis] -= 1
                moon2.velocity[axis] += 1
            elif value2 > value1:
                moon2.velocity[axis] -= 1
                moon1.velocity[axis] += 1

    def _apply_velocity(self):
        for moon in self.moons:
            moon.apply_velocity()

    def _least_common_multiple_for_pair(self, a, b):
        return int(abs(a*b) / math.gcd(int(a), int(b)))

    def _least_common_multiple(self, *numbers):
        return reduce(self._least_common_multiple_for_pair, numbers)


if __name__ == '__main__':
    moons = Moons(
                Moon([-4, 3, 15]),
                Moon([-11, -10, 13]),
                Moon([2, 2, 18]),
                Moon([7, -1, 0]),
            )
    moons.run_simulation(steps=1000)
    print('Total energy: ', moons.total_energy())

    moons = Moons(
                Moon([-4, 3, 15]),
                Moon([-11, -10, 13]),
                Moon([2, 2, 18]),
                Moon([7, -1, 0]),
            )
    print('Steps before repetition: ', moons.steps_until_repetition())

