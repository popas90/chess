import abc
from enum import Enum


class Color(Enum):
    """
    Enumeration for available colors.
    """
    White = 0
    Black = 1


class Direction(Enum):
    Forward = 0
    Back = 1
    Left = 2
    Right = 3


class InvalidMoveException(Exception):
    pass


class Piece:
    """
    Abstract class for a chess piece.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, piece_color, piece_location):
        """
        Constructor for setting all general piece properties.
        :param color: the piece's color (white or black)
        :param location: dictionary representing the piece's position
        :return: the new Piece object
        """
        self.location = piece_location
        self.color = piece_color
        self.moves = []

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
    def is_legal_move(self, new_location):
        return

    @abc.abstractmethod
    def get_all_legal_moves(self):
        return
