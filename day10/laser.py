import itertools

from math import pi
from monitoring_station import *
from collections import defaultdict

RHO = 0
PHI = 1

def distance(from_coordinates, to_coordinates):
    x1, y1 = from_coordinates
    x2, y2 = to_coordinates
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

def group_by_phi(asteroids):
    grouped = defaultdict(list)

    asteroids = sorted(asteroids, key=lambda asteroid: asteroid[RHO])

    for asteroid in asteroids:
        grouped[asteroid[PHI]].append(asteroid)
    return grouped

def cartesian_coordinates(polar_coordinates):
    rho, phi = polar_coordinates
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return (int(round(x)), int(round(y)))

def absolute_coordinates(asteroid, center):
    ax, ay = asteroid
    cx, cy = center
    return (ax + cx, ay + cy)

def find_nth_destroyed(n, asteroids):
    center = best_position(asteroids)
    asteroids = [relative_coordinates(asteroid, center) for asteroid in asteroids]
    polar_asteroids = [polar_coordinates(asteroid) for asteroid in asteroids]

    asteroids_by_phi = group_by_phi(polar_asteroids)

    phis = sorted(list(asteroids_by_phi.keys()), key=lambda phi: phi + 2*pi if phi < -pi/2 else phi)

    count = 0
    for i in itertools.count():
        phi = phis[i % len(phis)]
        if not asteroids_by_phi[phi]:
            continue

        asteroid = asteroids_by_phi[phi].pop(0)

        print(absolute_coordinates(cartesian_coordinates(asteroid), center))
        if asteroid[0] == 0:
            continue

        count += 1

        if count == n:
            cartesian = cartesian_coordinates(asteroid)
            return absolute_coordinates(cartesian, center)
    
if __name__ == '__main__':
    coordinates = (28, 29)

    asteroids_map = open('input').read()
    asteroids = asteroids_from(asteroids_map)
    
    print(f'200th: {find_nth_destroyed(200, asteroids)}')
    
