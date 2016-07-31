from model.Piece import Piece
from model.Piece import Color
from model.MovesGenerator import generate_all_moves


class Pawn(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color)
        # TODO review en-passant rule
        self._directions = [('F', 'empty', 'capture'),
                            ('FF', 'empty', 'capture'),
                            ('FR', 'capture'),
                            ('FL', 'capture')]

    def is_legal_move(self, location, new_location):
        all_locations = generate_all_moves(self, location)
        if new_location in all_locations:
            return True
        return False

    def get_all_valid_moves(self):
        pass
