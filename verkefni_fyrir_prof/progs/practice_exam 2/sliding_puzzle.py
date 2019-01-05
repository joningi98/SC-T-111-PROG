DIM = 4
EMPTYSLOT = 0
QUIT = 0


def initialize_board():
    numbers = input().split(" ")
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board


def display(puzzle_board):
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()

# Your code goes here...


def find_number(board, number):
    for x, row in enumerate(board):
        for y, num in enumerate(row):
            if number == num:
                return x, y


def move_number(board, x, y):
    try:
        if board[x][y + 1] == 0:
            board[x][y + 1] = board[x][y]
            board[x][y] = 0
        if board[x][y - 1] == 0:
            board[x][y - 1] = board[x][y]
            board[x][y] = 0
        if board[x + 1][y] == 0:
            board[x + 1][y] = board[x][y]
            board[x][y] = 0
        if board[x - 1][y] == 0:
            board[x - 1][y] = board[x][y]
            board[x][y] = 0
        return board
    except IndexError:
        print()


def main():
    board = initialize_board()
    display(board)
    game = True
    while game:
        number = int(input(""))
        if number == QUIT:
            quit()
        x, y = find_number(board, number)
        board = move_number(board, x, y)
        display(board)


main()