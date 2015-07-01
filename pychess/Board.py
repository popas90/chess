from pychess.Pawn import Pawn
from pychess.Rook import Rook
from pychess.Bishop import Bishop
from pychess.Knight import Knight
from pychess.Queen import Queen
from pychess.King import King
from pychess.Piece import *


class Direction(Enum):
    N = 0
    E = 1
    S = 2
    V = 3
    NV = 4
    NE = 5
    SV = 6
    SE = 7
    NS = 8
    EV = 9


class Board:

    def __init__(self):
        """

        :return:
        """
        state = self.reset_state()

    def reset_state(self):
        """

        :return:
        """
        board = {}
        for column in Col:
            for row in range(1, 8):
                location_dict = {"col" : column, "row" : row}
                if row in (2, 7):
                    board[column][row] = Pawn(Color.white if row == 2 else Color.black, location_dict, True)
                elif row in (1, 8):
                    if column in (Col.A, Col.H):
                        board[column][row] = Rook(Color.white if row == 1 else Color.black, location_dict, True)
                    elif column in (Col.B, Col.G):
                        board[column][row] = Knight(Color.white if row == 1 else Color.black, location_dict, True)
                    elif column in (Col.C, Col.F):
                        board[column][row] = Bishop(Color.white if row == 1 else Color.black, location_dict, True)
                    elif column == Col.D:
                        board[column][row] = Queen(Color.white if row == 1 else Color.black, location_dict, True)
                    else:
                        board[column][row] = King(Color.white if row == 1 else Color.black, location_dict, True)
        return board

    def is_clear_path(self, old_location, new_location):
        """

        :param old_location:
        :param new_location:
        :return:
        """