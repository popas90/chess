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

# TODO both this and MovesGenerator should be singletons


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
        self._state['a1'] = Rook(Color.White)
        self._state['b1'] = Knight(Color.White)
        self._state['c1'] = Bishop(Color.White)
        self._state['d1'] = Queen(Color.White)
        self._state['e1'] = King(Color.White)
        self._state['f1'] = Bishop(Color.White)
        self._state['g1'] = Knight(Color.White)
        self._state['h1'] = Rook(Color.White)

        self._state['a8'] = Rook(Color.Black)
        self._state['b8'] = Knight(Color.Black)
        self._state['c8'] = Bishop(Color.Black)
        self._state['d8'] = Queen(Color.Black)
        self._state['e8'] = King(Color.Black)
        self._state['f8'] = Bishop(Color.Black)
        self._state['g8'] = Knight(Color.Black)
        self._state['h8'] = Rook(Color.Black)

        for col in COLUMNS:
            self._state[col + '2'] = Pawn(Color.White)
            self._state[col + '7'] = Pawn(Color.Black)

    def is_location_empty(self, location):
        validate_location_string(location)
        return True if self._state[location] is None else False

    def move(self, location, new_location):
        # TODO these validations can be moved one level higher
        validate_location_string(location)
        validate_location_string(new_location)
        if self[location] is None:
            raise EmptyLocationException
        if self[location].is_legal_move(location, new_location):
            self._execute_move(location, new_location)

    def _execute_move(self, location, new_location):
        self._state[new_location] = self._state[location]
        self._state[location] = None
