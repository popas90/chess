from model.Piece import Piece


class Rook(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color)
        self._directions = [('F', 'repeat', 'empty', 'capture'),
                            ('R', 'repeat', 'empty', 'capture'),
                            ('B', 'repeat', 'empty', 'capture'),
                            ('L', 'repeat', 'empty', 'capture')]

    def move(self, new_location):
        if self.is_valid_move(new_location):
            self.location = new_location

    def is_valid_move(self, new_location):
        return True
