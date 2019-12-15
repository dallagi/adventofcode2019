from intcode import IntCodeVM, read_input
from collections import defaultdict

class Panel:
    BLACK = 0
    WHITE = 1

    CHARS = { BLACK: ' ', WHITE: '█' }

    def __init__(self, initial_color):
        self.plates_colors = defaultdict(lambda: self.BLACK)
        self.paint((0, 0), initial_color)

    def paint(self, coordinates, color):
        self.plates_colors[coordinates] = color

    def color(self, coordinates):
        return self.plates_colors[coordinates]

    def painted_plates_count(self):
        return len(self.plates_colors)

    def draw_to_stdout(self):
        plates = list(self.plates_colors.keys())
        xs = [plate[0] for plate in plates]
        ys = [plate[1] for plate in plates]

        for y in range(max(ys), min(ys)-1, -1):
            for x in range(min(xs), max(xs)+1):
                color = self.color((x, y))
                print(self.CHARS[color], end='')
            print()

class Robot:
    LEFT = 0
    RIGHT = 1

    DIRECTIONS = {
            'up': (0, 1),
            'right': (1, 0),
            'down': (0, -1),
            'left': (-1, 0)
            }

    def __init__(self, program, panel):
        self.vm = IntCodeVM(program, [])
        self.position = (0, 0)
        self.direction = self.DIRECTIONS['up']
        self.panel = panel

    def run(self):
        while True:
            if self.vm.finished():
                return

            self.vm.add_input(self.panel.color(self.position))

            color = next(self.vm.run())
            direction = next(self.vm.run())
        
            self.panel.paint(self.position, color)
            self.move(direction)
    
    def move(self, direction):
        if direction == self.LEFT:
            if self.direction == self.DIRECTIONS['up']:
                self.direction = self.DIRECTIONS['left']
            elif self.direction == self.DIRECTIONS['left']:
                self.direction = self.DIRECTIONS['down']
            elif self.direction == self.DIRECTIONS['down']:
                self.direction = self.DIRECTIONS['right']
            elif self.direction == self.DIRECTIONS['right']:
                self.direction = self.DIRECTIONS['up']
        if direction == self.RIGHT:
            if self.direction == self.DIRECTIONS['up']:
                self.direction = self.DIRECTIONS['right']
            elif self.direction == self.DIRECTIONS['right']:
                self.direction = self.DIRECTIONS['down']
            elif self.direction == self.DIRECTIONS['down']:
                self.direction = self.DIRECTIONS['left']
            elif self.direction == self.DIRECTIONS['left']:
                self.direction = self.DIRECTIONS['up']

        px, py = self.position
        dx, dy = self.direction
        self.position = (px+dx, py+dy)


if __name__ == '__main__':
    program = read_input()

    # part 1
    panel = Panel(initial_color=Panel.BLACK)
    robot = Robot(program, panel)
    robot.run()
    print(f'Number of plates painted: {panel.painted_plates_count()}')

    # part 2
    panel = Panel(initial_color=Panel.WHITE)
    robot = Robot(program, panel)
    robot.run()
    panel.draw_to_stdout()

