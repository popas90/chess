from model.Board import Board
from model.Piece import InvalidMoveException
from model.Location import Location, InvalidLocationException


class TextPresenter:

    def __init__(self):
        self._board = Board()

    def get_piece_from_location(self, location):
        return self._board.get_piece_from_location(location)

    def print_board(self):
        for i in range(7, -1, -1):
            row = str(i+1) + ' '
            for j in range(7, -1, -1):
                piece_on_location = self.get_piece_from_location((i, j))
                if (i+j) % 2 == 1:
                    row += ' ' + piece_on_location + ' '
                else:
                    row += '[' + piece_on_location + ']'
            print(row)
        final_row = '   A  B  C  D  E  F  G  H'
        print(final_row)

    def move_piece(self, loc_str, new_loc_str):
        try:
            location = Location(loc_str)
            new_location = Location(new_loc_str)
            self.move(location, new_location)
        except (InvalidMoveException, InvalidLocationException):
            print('Invalid move: ' + loc_str +
                  ' -> ' + new_loc_str)

    def validate_move(self, location, new_location):
        pass

    def move(self, location, new_location):
        self.validate_move(location, new_location)
        self._board.get_piece_from_location()
