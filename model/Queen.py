from model.Piece import Piece


class Queen(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color)
        self._directions = [('F', 'repeat'),
                            ('FR', 'repeat'),
                            ('R', 'repeat'),
                            ('BR', 'repeat'),
                            ('B', 'repeat'),
                            ('BL', 'repeat'),
                            ('L', 'repeat'),
                            ('FL', 'repeat')]

    def move(self, new_location):
        if self.is_valid_move(new_location):
            self.location = new_location

    def is_valid_move(self, new_location):
        return True
