from model.Piece import Piece
from model.Piece import Color


class Pawn(Piece):

    def __init__(self, piece_color, piece_location):
        super().__init__(piece_color, piece_location)
        self.moves = [('F'),
                      ('FF'),
                      ('FR', 'capture'),
                      ('FL', 'capture')]

    def move(self, new_location):
        """
        Changes the location of the piece to the new location.
        :param new_location: tuple specifying column and row.
        :return: True if piece was moved.
        """
        if self.is_legal_move(new_location):
            self.location = new_location

    def is_valid_move(self, new_location):
        """
        True if piece can be legally moved to the new location.
        :param new_location: tuple of new location
        :return: True if move is valid
        """
        if (self.location["col"] == new_location["col"]):
            # Moving forward means incrementing the row
            if (self.color == Color.white and 1 <= new_location["row"] - self.location["row"] <= 2):
                return True
            if (self.color == Color.black and 1 <= self.location["row"] - new_location["row"] <= 2):
                return True

    def get_all_valid_moves(self):
        """

        :return:
        """
