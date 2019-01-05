# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'


def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')

    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move


def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid


# Main program starts here
# In your implementation, you have to use the functions and the constants given above

def display_grid(grid):
    for x in grid:
        print(*x)
    print()


def find_position(grid, POSITION):
    for x, row in enumerate(grid):
        for y, obj in enumerate(row):
            if obj == POSITION:
                return x, y


def main():
    grid = initialize_grid()
    display_grid(grid)
    game = True
    while game:
        try:
            move = get_move()
            if move == QUIT:
                quit()
            x, y = find_position(grid, POSITION)
            if move == RIGHT:
                grid[x][y + 1] = "o"
            if move == LEFT:
                grid[x][y - 1] = "o"
            if move == UP:
                grid[x - 1][y] = "o"
            if move == DOWN:
                grid[x + 1][y] = "o"
            grid[x][y] = EMPTY
            display_grid(grid)
        except IndexError:
            pass


main()
