
class PlanetsTree:
    def __init__(self, name, orbited_by=None):
        self.name = name
        self.orbited_by = orbited_by or []

    @classmethod
    def from_orbits(cls, orbits, name):
        planet = cls(name)
        for orbit in orbits:
            target, orbiter = orbit.strip().split(')')
            if target == name:
                planet.orbited_by.append(cls.from_orbits(orbits, orbiter))

        return planet

def total_number_of_orbits(planet_tree, orbits, level=1):
    if planet_tree is None:
        return 0

    return sum(level + total_number_of_orbits(space_object, orbits, level+1)
            for space_object in planet_tree.orbited_by)
    

if __name__ == '__main__':
    input_orbits = open('input').readlines()
    planets_tree = build_planets_tree(input_orbits, 'COM')
    
    orbits_count = total_number_of_orbits(planets_tree, input_orbits)

    print(f"Total number of orbits: {orbits_count}")
