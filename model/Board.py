from model.LocationValidator import validate_location_string
from model.LocationValidator import COLUMNS, ROWS
from model.Piece import Color
from model.Rook import Rook
from model.Knight import Knight
from model.Bishop import Bishop
from model.Queen import Queen
from model.King import King
from model.Pawn import Pawn


class InvalidMoveException(Exception):
    pass


class EmptyLocationException(Exception):
    pass


class Board:

    SQUARES = [str(col + row)
               for col in COLUMNS
               for row in ROWS]

    def __init__(self):
        self._state = {n: None for n in Board.SQUARES}

    def __getitem__(self, location):
        validate_location_string(location)
        return self._state[location]

    def _populate_with_default(self):
        self._state['a1'] = Rook(Color.White, 'a1')
        self._state['b1'] = Knight(Color.White, 'b1')
        self._state['c1'] = Bishop(Color.White, 'c1')
        self._state['d1'] = Queen(Color.White, 'd1')
        self._state['e1'] = King(Color.White, 'e1')
        self._state['f1'] = Bishop(Color.White, 'f1')
        self._state['g1'] = Knight(Color.White, 'g1')
        self._state['h1'] = Rook(Color.White, 'h1')

        self._state['a8'] = Rook(Color.Black, 'a8')
        self._state['b8'] = Knight(Color.Black, 'b8')
        self._state['c8'] = Bishop(Color.Black, 'c8')
        self._state['d8'] = Queen(Color.Black, 'd8')
        self._state['e8'] = King(Color.Black, 'e8')
        self._state['f8'] = Bishop(Color.Black, 'f8')
        self._state['g8'] = Knight(Color.Black, 'g8')
        self._state['h8'] = Rook(Color.Black, 'h8')

        for col in COLUMNS:
            self._state[col + '2'] = Pawn(Color.White, col + '2')
            self._state[col + '7'] = Pawn(Color.Black, col + '7')

    def is_location_empty(self, location):
        validate_location_string(location)
        return True if self._state[location] is None else False

    def move(self, location, new_location):
        # TODO these validations can be moved one level higher
        validate_location_string(location)
        validate_location_string(new_location)
        if self[location] is None:
            raise EmptyLocationException
