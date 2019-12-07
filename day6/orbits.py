
class PlanetsTree:
    def __init__(self, name, orbited_by=None):
        self.name = name
        self.orbited_by = orbited_by or []

    @classmethod
    def from_orbits(cls, orbits, name='COM'):
        planet = cls(name)
        for orbit in orbits:
            target, orbiter = orbit.strip().split(')')
            if target == name:
                planet.orbited_by.append(cls.from_orbits(orbits, orbiter))

        return planet

    def total_number_of_orbits(self, level=1):
        return sum(level + space_object.total_number_of_orbits(level+1)
                for space_object in self.orbited_by)

    def minimum_number_of_orbital_transfers(self, start, end):
        nearest_common_parent = self._nearest_common_parent(start, end)
        
        return nearest_common_parent._child_depth(start) + nearest_common_parent._child_depth(end)

    def _nearest_common_parent(self, a, b):
        # very unefficient approach, but it works ¯\_(ツ)_/¯
        for space_object in self.orbited_by:
            if space_object._is_orbited_by(a) and space_object._is_orbited_by(b):
                return space_object._nearest_common_parent(a, b)
        return self

    def _is_orbited_by(self, target):
        if not self.orbited_by:
            return False
        if target in [space_object.name for space_object in self.orbited_by]:
            return True
        return any(space_object._is_orbited_by(target) for space_object in self.orbited_by)

    def _child_depth(self, target, accumulator=0):
        if not self.orbited_by:
            return 0
        if target in [space_object.name for space_object in self.orbited_by]:
            return accumulator
        return sum(space_object._child_depth(target, accumulator + 1) for space_object in self.orbited_by)

if __name__ == '__main__':
    input_orbits = open('input').readlines()
    planets_tree = PlanetsTree.from_orbits(input_orbits)
    
    print(f"Total number of orbits: {planets_tree.total_number_of_orbits()}")
    print(f"Minimum number of orbital transfers: {planets_tree.minimum_number_of_orbital_transfers('YOU', 'SAN')}")
