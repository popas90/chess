import nose
# from nose.tools import assert_raises
from model.Board import Board
from model.LocationValidator import validate_location_string
from model.LocationValidator import InvalidLocationException
from model.LocationValidator import COLUMNS
from model.Rook import Rook
from model.Knight import Knight
from model.Bishop import Bishop
from model.Queen import Queen
from model.King import King
from model.Pawn import Pawn
from model.Piece import Color
from model.Board import EmptyLocationException


def test_location_validator():
    nose.tools.eq_(validate_location_string("H8"), True)
    nose.tools.eq_(validate_location_string("f7"), True)
    nose.tools.assert_raises(InvalidLocationException,
                             validate_location_string, "DD6")
    nose.tools.assert_raises(InvalidLocationException,
                             validate_location_string, "K6")
    nose.tools.assert_raises(InvalidLocationException,
                             validate_location_string, "56")
    nose.tools.assert_raises(InvalidLocationException,
                             validate_location_string, "A9")
    nose.tools.assert_raises(InvalidLocationException,
                             validate_location_string, "d0")


def test_board_empty_state():
    board = Board()
    nose.tools.eq_(board['d4'], None)
    nose.tools.eq_(board['e2'], None)


def test_board_initial_state():
    board = Board()
    board._populate_with_default()
    nose.tools.ok_(isinstance(board['a1'], Rook))
    nose.tools.ok_(isinstance(board['b1'], Knight))
    nose.tools.ok_(isinstance(board['c1'], Bishop))
    nose.tools.ok_(isinstance(board['d1'], Queen))
    nose.tools.ok_(isinstance(board['e1'], King))
    nose.tools.ok_(isinstance(board['f1'], Bishop))
    nose.tools.ok_(isinstance(board['g1'], Knight))
    nose.tools.ok_(isinstance(board['h1'], Rook))
    nose.tools.ok_(isinstance(board['a8'], Rook))
    nose.tools.ok_(isinstance(board['b8'], Knight))
    nose.tools.ok_(isinstance(board['c8'], Bishop))
    nose.tools.ok_(isinstance(board['d8'], Queen))
    nose.tools.ok_(isinstance(board['e8'], King))
    nose.tools.ok_(isinstance(board['f8'], Bishop))
    nose.tools.ok_(isinstance(board['g8'], Knight))
    nose.tools.ok_(isinstance(board['h8'], Rook))

    for col in COLUMNS:
        nose.tools.ok_(isinstance(board[col + '2'], Pawn))
        nose.tools.ok_(isinstance(board[col + '7'], Pawn))
        nose.tools.eq_(board[col + '1'].color, Color.White)
        nose.tools.eq_(board[col + '2'].color, Color.White)
        nose.tools.eq_(board[col + '3'], None)
        nose.tools.eq_(board[col + '4'], None)
        nose.tools.eq_(board[col + '5'], None)
        nose.tools.eq_(board[col + '6'], None)
        nose.tools.eq_(board[col + '7'].color, Color.Black)
        nose.tools.eq_(board[col + '8'].color, Color.Black)


def test_board_is_location_empty():
    board = Board()
    nose.tools.ok_(board.is_location_empty("d2"))
    nose.tools.ok_(board.is_location_empty("a1"))
    nose.tools.ok_(board.is_location_empty("h7"))


def test_board_move_exceptions():
    board = Board()
    board._populate_with_default()
    nose.tools.assert_raises(InvalidLocationException,
                             board.move, 'dg3', 'd4')
    nose.tools.assert_raises(EmptyLocationException,
                             board.move, 'd3', 'd4')
    nose.tools.assert_raises(EmptyLocationException,
                             board.move, 'd5', 'd2')
