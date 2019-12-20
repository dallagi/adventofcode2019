from intcode import IntCodeVM, read_input

class Grid:
    def __init__(self):
        self.grid = {}

    def set(self, x, y, tile):
        self.grid[(x, y)] = tile

    def count_of_tiles_of_type(self, tile_type):
        return sum([grid_tile_type == tile_type for grid_tile_type in self.grid.values()])

    def get_position_of(self, tile_type):
        for position in self.grid:
            if self.grid[position] == tile_type:
                return position

class Arcade:
    BLOCK_TILE = 2
    PADDLE_TILE = 3
    BALL_TILE = 4

    JOYSTICK_NEUTRAL = 0
    JOYSTICK_LEFT = -1
    JOYSTICK_RIGHT = 1

    def __init__(self, program, play_for_free=False, debug=False):
        if play_for_free:
            program = self._remove_check_for_quarters(program)
        self.debug = debug
        self.vm = IntCodeVM(program)
        self.grid = Grid()

        self.joystick_direction = self.JOYSTICK_NEUTRAL
        self.score = None

    def run_instruction(self):
        x, y, value = self.get_instruction()
        if self.is_score(x, y):
            self.score = value
            self._debug(f"Setting score to {value}")
        else:
            self._debug(f'Setting tile of type {value} to ({x}, {y})')
            self.set_tile(x, y, value)
            self.play()

    def play(self):
        self._debug(f'Paddle: {self.paddle_position()}, Ball: {self.ball_position()}, Direction: {self.joystick_direction}')

        if None in [self.paddle_position(), self.ball_position()]:
            return
        if self.paddle_position()[0] > self.ball_position()[0]:
            self.move_joystick(self.JOYSTICK_LEFT)
        elif self.paddle_position()[0] < self.ball_position()[0]:
            self.move_joystick(self.JOYSTICK_RIGHT)
        else:
            self.move_joystick(self.JOYSTICK_NEUTRAL)

    def is_score(self, x, y):
        return x == -1 and y == 0

    def set_tile(self, x, y, tile):
        self.grid.set(x, y, tile)
    
    def get_instruction(self):
        return list(next(self.vm.run()) for _ in range(3))

    def run(self):
        while not self.vm.finished():
            self.vm.set_input(self.joystick_direction)
            self.run_instruction()

    def blocks_count(self):
        return self.grid.count_of_tiles_of_type(self.BLOCK_TILE)

    def ball_position(self):
        return self.grid.get_position_of(self.BALL_TILE)

    def paddle_position(self):
        return self.grid.get_position_of(self.PADDLE_TILE)

    def move_joystick(self, direction):
        assert(direction in [self.JOYSTICK_LEFT, self.JOYSTICK_NEUTRAL, self.JOYSTICK_RIGHT])

        self.joystick_direction = direction

    def _remove_check_for_quarters(self, program):
        program[0] = 2
        return program

    def _debug(self, message):
        if self.debug:
            print('[DEBUG] ' + message)


if __name__ == '__main__':
    arcade = Arcade(read_input())

    arcade.run()
    print(f'Block tiles on screen: {arcade.grid.count_of_tiles_of_type(2)}')

    arcade = Arcade(read_input(), play_for_free=True)
    arcade.run()
    print(f'Score: {arcade.score}')
