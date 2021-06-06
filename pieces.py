class Piece:
    is_white = False
    rank = 0
    file = 0

    def __init__(self, is_white, rank, file):
        self.is_white = is_white
        self.rank = rank
        self.file = file


class Knight(Piece):
    def get_moves(self):
        pass


class Rook(Piece):
    def get_moves(self):
        pass


class Bishop(Piece):
    def get_moves(self):
        pass


class Queen(Piece):
    def get_moves(self):
        pass


class King(Piece):
    def get_moves(self):
        pass


class Pawn(Piece):
    def get_moves(self):
        pass
