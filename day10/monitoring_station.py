import numpy as np
from fractions import Fraction

def asteroids_from(asteroids_map):
    asteroids = []
    rows = asteroids_map.strip().split('\n')
    for row_index, row in enumerate(rows):
        for char_index, char in enumerate(row):
            if char == '#':
                asteroids.append((char_index, row_index))
    return asteroids

def relative_coordinates(point, center):
    pX, pY = point
    cX, cY = center
    return (pX-cX, pY-cY)

def aligned(asteroid1, asteroid2):
    return asteroid1[1] == asteroid2[1]

def polar_coordinates(asteroid):
    x, y = asteroid
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return (rho, phi)

def seen_asteroids_count(asteroids, coordinates):
    relative_coords_asteroids = [relative_coordinates(asteroid, coordinates) for asteroid in asteroids]
    polar_coords_asteroids = [polar_coordinates(asteroid) for asteroid in relative_coords_asteroids]
    
    seen_asteroids = []

    for asteroid in polar_coords_asteroids:
        if any(aligned(asteroid, other) for other in seen_asteroids):
            continue
        seen_asteroids.append(asteroid)

    return len(seen_asteroids)

def best_position(asteroids):
    best_location = None
    max_seen = -1
    for asteroid in asteroids:
        #  print(f'Trying {asteroid}', end="")

        seen_asteroids = seen_asteroids_count(asteroids, asteroid)
        #  print(' -> ', seen_asteroids)
        if seen_asteroids > max_seen:
            max_seen = seen_asteroids
            best_location = asteroid
    return best_location

if __name__ == '__main__':
    asteroids_map = open('input').read()
    asteroids = asteroids_from(asteroids_map)

    print(seen_asteroids_count(asteroids, (32, 3)))
    location = best_position(asteroids)

    print(f'Best location: {location}')
