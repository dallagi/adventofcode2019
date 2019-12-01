import math

def masses_from_file():
    return [int(line) for line in open('input').readlines()]

def fuel_for(mass):
    return math.floor(mass / 3) - 2

def total_fuel_for(mass, total=0):
    fuel = fuel_for(mass)
    if fuel <= 0:
        return total
    return total_fuel_for(fuel, total + fuel)

def required_fuel():
    return sum(fuel_for(module_mass) for module_mass in masses_from_file())

def total_required_fuel():
    return sum(total_fuel_for(module_mass) for module_mass in masses_from_file())

if __name__ == '__main__':
    print(f"Basic fuel requirement: {required_fuel()}")
    print(f"Total fuel requirement: {total_required_fuel()}")
