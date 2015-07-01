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

    def __init__(self, color, location, board):
        """
        Constructor for setting all general piece properties.
        :param color: the piece's color (white or black)
        :param location: dictionary representing the piece's position on the board
        :param board: reference to the current board
        :return: the new Piece object
        """
        self.location = location
        self.board = board
        self.color = color
        self.col_index = 0
        self.row_index = 1

    @property
    def location(self):
        return self.location

    @location.setter
    def location(self, value):
        self.location = value

    @property
    def on_board(self):
        return self.board

    @abc.abstractmethod
    def move(self, new_location):
        return

    @abc.abstractmethod
    def is_valid_move(self, new_location):
        return

    @abc.abstractmethod
    def get_all_valid_moves(self):
        return
