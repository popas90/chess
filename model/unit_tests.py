import nose
from model.Board import Board
from model.Location import Location
from model.Location import InvalidLocationException


def test_location_invalid():
    nose.tools.assert_raises(InvalidLocationException, Location, "DD6")
    nose.tools.assert_raises(InvalidLocationException, Location, "K6")
    nose.tools.assert_raises(InvalidLocationException, Location, "56")
    nose.tools.assert_raises(InvalidLocationException, Location, "A9")
    nose.tools.assert_raises(InvalidLocationException, Location, "d0")


def test_board_initial_state():
    board = Board()
    nose.tools.eq_(board._state[0], 'RNBKQBNR')
    nose.tools.eq_(board._state[1], 'PPPPPPPP')
    nose.tools.eq_(board._state[2], '........')
    nose.tools.eq_(board._state[3], '........')
    nose.tools.eq_(board._state[4], '........')
    nose.tools.eq_(board._state[5], '........')
    nose.tools.eq_(board._state[6], 'pppppppp')
    nose.tools.eq_(board._state[7], 'rnbkqbnr')


def test_board_get_piece_initial_state():
    board = Board()
    nose.tools.eq_(board.get_piece((0, 0)), 'R')
    nose.tools.eq_(board.get_piece((0, 1)), 'N')
