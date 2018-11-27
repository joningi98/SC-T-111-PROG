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



def print_grid(grid):
    for x in grid:
        print(*x)


def user_choice(move):
    if move == 'l':
        current_pos = left()
    if move == 'r':
        current_pos = right()
    if move == 'u':
        current_pos = upp()
    if move == 'd':
        current_pos = down()


def left(current_pos):
    c = current_pos - 1
    return c


def right(current_pos):
    c = current_pos + 1
    return c

def upp():
    pass


def down():
    pass


def main():
    grid = initialize_grid()
    print_grid(grid)
    current_pos = grid[1][0]
    while True:
        move = get_move()


main()
