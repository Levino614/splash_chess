def create_board():
    chess_board = []
    for i in range(8):
        rank = []
        for j in range(8):
            is_dark_square = (i + j) % 2 != 0
            rank.append(is_dark_square)
        chess_board.append(rank)
    return chess_board


board = create_board()

for row in board:
    print(row)
