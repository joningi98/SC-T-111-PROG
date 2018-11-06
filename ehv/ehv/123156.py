def board_dimension():
    while True:
        try:
            dimension = int(input("Input dimension of the board: "))
            if dimension < 3:
                continue
            board = [[] for _ in range(dimension)]
            length = dimension**2
            for i in range(1, length + 1):
                if len(board[0]) != dimension:
                    board[0].append(i)
                elif len(board[1]) != dimension:
                    board[1].append(i)
                else:
                    board[2].append(i)
            print(board)
            print_board(board)
            return board, length
        except ValueError:
            print('')
