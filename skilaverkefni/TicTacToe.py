def board_dimension():
    condition = True
    while condition:
        try:
            dimension = int(input("Input dimension of the board: "))
            if dimension < 3:
                continue
            return dimension
        except ValueError:
            print('')


def build_board(dimension):
    counter = 1
    board = []
    for x in range(dimension):
        board_2 = []
        for y in range(dimension):
            board_2.append(counter)
            counter += 1
        board.append(board_2)
    print_board(board)
    return board


def player_(board, user):
    turn = True
    while turn:  # Try until a player inputs a correct location for user
        n = int(input('{} position: '.format(user)))
        for x, row in enumerate(board):
            for y, value in enumerate(row):
                if value == n:
                    board[x][y] = user
                    print_board(board)
                    return
                else:
                    continue
        print("Illegal move!")


def print_board(board):
    for x in range(len(board)):
        for y in range(len(board)):
            print('{:>5}'.format(board[x][y]), end=' ')
        print('')


def check_if_draw_game(board, length):
    counter = 0
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if board[x][y] == 'X' or board[x][y] == 'O':
                counter += 1
                if counter == length:
                    return True


def check_if_victory(board, dimension, user):
    player_list = []
    copy_board = board[:]
    copy_board.reverse()
    for s in range(dimension):
        player_list.append(user)
    if (['X'] * dimension) in board or (['O'] * dimension) in board:
        return True
    for x in range(dimension):
        win_list = []
        for y in range(dimension):
            win_list.append(board[y][y])
        if win_list == player_list:
            return True
    for i in range(dimension):
        win_list_2 = []
        for j in range(dimension):
            win_list_2.append(copy_board[j][j])
        if win_list_2 == player_list:
            return True
    for h in range(dimension):
        win_list_3 = []
        for l in range(dimension):
            win_list_3.append(board[l][h])
            if win_list_3 == player_list:
                return True


def main():
    dimension = board_dimension()
    board = build_board(dimension)
    end = True
    while end:
        for user in ['X', 'O']:
            player_(board, user)
            if check_if_victory(board, dimension, user):
                print('Winner is: {}'.format(user))
                quit()
            if check_if_draw_game(board, dimension**2):
                print("Draw!")
                quit()


main()
