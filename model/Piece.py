import abc
from enum import Enum


class Color(Enum):
    """
    Enumeration for available colors.
    """
    White = 0
    Black = 1


class Piece:
    """
    Abstract class for a chess piece.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, piece_color):
        """
        Constructor for setting all general piece properties.
        :param color: the piece's color (white or black)
        :return: the new Piece object
        """
        self.color = piece_color
        self._directions = []

    @property
    def directions(self):
        return self._directions

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
        """
        Changes the location of the piece to the new location.
        :param new_location: tuple specifying column and row.
        :return: True if piece was moved.
        """
        pass

    @abc.abstractmethod
    def is_legal_move(self, new_location):
        """
        True if piece can be legally moved to the new location.
        :param new_location: tuple of new location
        :return: True if move is valid
        """
        pass

    @abc.abstractmethod
    def get_all_legal_moves(self):
        return
