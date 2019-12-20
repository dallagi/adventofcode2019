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
    BALL_TILE = 4

    JOYSTICK_NEUTRAL = 0
    JOYSTICK_LEFT = -1
    JOYSTICK_RIGHT = 1

    def __init__(self, program):
        self.vm = IntCodeVM(program)
        self.grid = Grid()

    def process_tile(self):
        x, y, tile = self.get_tile()
        self.grid.set(x, y, tile)
    
    def get_tile(self):
        return list(next(self.vm.run()) for _ in range(3))

    def run(self):
        while not self.vm.finished():
            self.process_tile()

    def blocks_count(self):
        return self.grid.count_of_tiles_of_type(self.BLOCK_TILE)

    def ball_position(self):
        return self.grid.get_position_of(self.BALL_TILE)

    def move_joystick(self, direction):
        assert(direction in [self.JOYSTICK_LEFT, self.JOYSTICK_NEUTRAL, self.JOYSTICK_RIGHT])

        self.vm.add_input(direction)

    def _remove_check_for_quarters(self, program):
        program[0] = 2
        return program

if __name__ == '__main__':
    arcade = Arcade(read_input())

    arcade.run()
    print(f'Block tiles on screen: {arcade.grid.count_of_tiles_of_type(2)}')
