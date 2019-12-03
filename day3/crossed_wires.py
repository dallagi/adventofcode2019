from collections import namedtuple

Direction = namedtuple('Direction', 'axis negative_distance')

DIRECTIONS = {
    'U': Direction(axis=1, negative_distance=False),
    'R': Direction(axis=0, negative_distance=False),
    'D': Direction(axis=1, negative_distance=True),
    'L': Direction(axis=0, negative_distance=True)
}

def visited_points(movements):
    visited = [(0, 0)]

    for movement in movements:
        direction = DIRECTIONS[movement[0]]
        distance = int(movement[1:])
    
        for _ in range(distance):
            last_point = visited[-1]
            current_point = list(last_point)
            if direction.negative_distance:
                current_point[direction.axis] -= 1
            else:
                current_point[direction.axis] += 1
            visited.append(tuple(current_point))

    return visited

def distance_from_central_point(point):
    return abs(point[0]) + abs(point[1])

def combined_steps_to_reach(intersection, visited_by_first_wire, visited_by_second_wire):
    first_wire_steps = visited_by_first_wire.index(intersection)
    second_wire_steps = visited_by_second_wire.index(intersection)
    return first_wire_steps + second_wire_steps

def main():
    movements = open('input').readlines()

    visited_by_first_wire = visited_points(movements[0].split(','))
    visited_by_second_wire = visited_points(movements[1].split(','))

    intersections = set(visited_by_first_wire).intersection(set(visited_by_second_wire))
    intersections.discard((0, 0))

    manhattan_distances = [distance_from_central_point(point) for point in intersections]
    print(f'Minimum manhattan distance: {min(manhattan_distances)}')
    combined_steps_for_intersections = [combined_steps_to_reach(intersection, visited_by_first_wire, visited_by_second_wire)
                                        for intersection in intersections]
                                
    print(f'Minimum combined steps: {min(combined_steps_for_intersections)}')
    
if __name__ == '__main__':
    main()