import math
from fractions import Fraction

def asteroids_from(asteroids_map):
    asteroids = []
    rows = asteroids_map.strip().split('\n')
    for row_index, row in enumerate(rows):
        for char_index, char in enumerate(row):
            if char == '#':
                asteroids.append((char_index, row_index))
    return asteroids

def distance(from_coordinates, to_coordinates):
    x1, y1 = from_coordinates
    x2, y2 = to_coordinates
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def relative_coordinates(point, center):
    pX, pY = point
    cX, cY = center
    return (pX-cX, pY-cY)

def ratio_of(point):
    X, Y = point
    if X == 0 and Y == 0:
        return None
    if Y == 0:
        return 'inf'

    return Fraction(X, Y)

def quadrant(asteroid):
    x, y = asteroid
    return 10*(x>=0) + (y>=0)

def aligned(asteroid1, asteroid2):
    return ratio_of(asteroid1) == ratio_of(asteroid2) and quadrant(asteroid1) == quadrant(asteroid2)

def seen_asteroids_count(asteroids, coordinates):
    #  asteroids = sorted(asteroids, key=lambda asteroid: distance(coordinates, asteroid))
    relative_coords_asteroids = [relative_coordinates(asteroid, coordinates) for asteroid in asteroids]
    
    seen_asteroids = []

    for asteroid in relative_coords_asteroids:
        if asteroid == (0, 0):
            continue
        if any(aligned(asteroid, other) for other in seen_asteroids):
            continue
        seen_asteroids.append(asteroid)

    return len(seen_asteroids)

def best_position(asteroids):
    best_location = None
    max_seen = -1
    for asteroid in asteroids:
        print(f'Trying {asteroid}', end="")

        seen_asteroids = seen_asteroids_count(asteroids, asteroid)
        print(' -> ', seen_asteroids)
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
