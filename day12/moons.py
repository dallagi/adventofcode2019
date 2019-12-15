import copy
import itertools

from dataclasses import dataclass, field
from itertools import combinations
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

    def run_simulation(self, *, steps: int):
        for _ in range(steps):
            self._apply_gravity()
            self._apply_velocity()

    def total_energy(self):
        return sum(moon.total_energy() for moon in self.moons)

    def steps_until_repetition(self):
        for i in itertools.count():
            print(f'\r{i+1}', end='')
            self.run_simulation(steps=1)
            if tuple(self.moons) == tuple(self.initial_moons):
                print('\r{i+1}')
                return i+1

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

if __name__ == '__main__':
    moons = Moons(
                Moon([-4, 3, 15]),
                Moon([-11, -10, 13]),
                Moon([2, 2, 18]),
                Moon([7, -1, 0]),
            )
    moons.run_simulation(steps=1000)
    print('Total energy: ', moons.total_energy())

