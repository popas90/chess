from model.Piece import Piece


class Knight(Piece):

    def __init__(self, piece_color, piece_location):
        super().__init__(piece_color, piece_location)
        self.moves = [('FFR'),
                      ('FFL'),
                      ('RRF'),
                      ('RRB'),
                      ('LLF'),
                      ('LLB'),
                      ('BBL'),
                      ('BBR')]

    def move(self, new_location):
        if self.is_valid_move(new_location):
            self.location = new_location

    def is_valid_move(self, new_location):
        return True
