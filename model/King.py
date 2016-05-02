from model import Piece


class King(Piece):
    def __init__(self, piece_color, piece_location):
        super().__init__(piece_color, piece_location)
        self.moves = [('F'),
                      ('FR'),
                      ('R'),
                      ('BR'),
                      ('B'),
                      ('B L'),
                      ('L'),
                      ('FL')]

    def move(self, new_location):
        if self.is_valid_move(new_location):
            self.location = new_location

    def is_valid_move(self, new_location):
        return True
