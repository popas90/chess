import nose
from nose.tools import raises
from model.Board import Board
from model.Location import Location
from model.Location import InvalidLocationException


def test_location_invalid():
    nose.tools.assert_raises(InvalidLocationException, Location, "DD6")
    nose.tools.assert_raises(InvalidLocationException, Location, "K6")
    nose.tools.assert_raises(InvalidLocationException, Location, "56")
    nose.tools.assert_raises(InvalidLocationException, Location, "A9")
    nose.tools.assert_raises(InvalidLocationException, Location, "d0")


def test_location_str():
    nose.tools.eq_(str(Location("D6")), "d6")
    nose.tools.eq_(str(Location("d6")), "d6")
    nose.tools.eq_(str(Location("a1")), "a1")
    nose.tools.eq_(str(Location("B8")), "b8")
    nose.tools.eq_(str(Location("C3")), "c3")
    nose.tools.eq_(str(Location("D7")), "d7")
    nose.tools.eq_(str(Location("E4")), "e4")
    nose.tools.eq_(str(Location("f6")), "f6")
    nose.tools.eq_(str(Location("g5")), "g5")
    nose.tools.eq_(str(Location("H2")), "h2")


def test_location_repr():
    nose.tools.eq_(repr(Location("D6")), "Location: d6")
    nose.tools.eq_(repr(Location("g5")), "Location: g5")


def test_location_properties():
    nose.tools.eq_(Location("b2").column, "b")
    nose.tools.eq_(Location("B5").column, "b")
    nose.tools.eq_(Location("A2").column, "a")
    nose.tools.eq_(Location("b2").row, "2")
    nose.tools.eq_(Location("E3").row, "3")
    nose.tools.eq_(Location("A8").row, "8")


@raises(AttributeError)
def test_location_column_setter():
    Location("b2").column = "c"


@raises(AttributeError)
def test_location_row_setter():
    Location("b2").row = "2"


def test_board_initial_state():
    board = Board()
    nose.tools.eq_(board['d4'], None)
    nose.tools.eq_(board['e2'], None)
    board._populate_with_default()
