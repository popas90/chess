import abc
from enum import Enum


class Color(Enum):
    """
    Enumeration for available colors.
    """
    white = 0
    black = 1


class Col(Enum):
    """
    Enumeration for board columns coding.
    """
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8


class Piece:
    """
    Abstract class for a chess piece.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, piece_color, piece_location):
        """
        Constructor for setting all general piece properties.
        :param color: the piece's color (white or black)
        :param location: dictionary representing the piece's position on the board
        :return: the new Piece object
        """
        self.location = piece_location
        self.color = piece_color

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @abc.abstractmethod
    def move(self, new_location):
        return

    @abc.abstractmethod
    def is_valid_move(self, new_location):
        return

    @abc.abstractmethod
    def get_all_valid_moves(self):
        return
