from model.Piece import Piece


class Bishop(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color)
        self._directions = [('FR', 'repeat'),
                            ('FL', 'repeat'),
                            ('BR', 'repeat'),
                            ('BL', 'repeat')]

    def move(self, new_location):
        if self.is_valid_move(new_location):
            self.location = new_location

    def is_valid_move(self, new_location):
        return True
