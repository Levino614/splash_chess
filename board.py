def CreateBoard():
    chessBoard = []
    for i in range(8):
        rank = []
        for j in range(8):
            isDarksquare = (i + j) % 2 != 0
            rank.append(isDarksquare)
        chessBoard.append(rank)
    return chessBoard


board = CreateBoard()

for row in board:
    print(row)
