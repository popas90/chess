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
        self.reset_board()

    def reset_board(self):
        """

        :return:
        """
        self.board = {}
        for column in Col:
            for row in range(1, 8):
                location_dict = {"col" : column, "row" : row}
                if row in (2, 7):
                    self.board[column][row] = Pawn(Color.white if row == 2 else Color.black, location_dict, True)
                elif row in (1, 8):
                    if column in (Col.A, Col.H):
                        self.board[column][row] = Rook(Color.white if row == 1 else Color.black, location_dict, True)
                    elif column in (Col.B, Col.G):
                        self.board[column][row] = Knight(Color.white if row == 1 else Color.black, location_dict, True)
                    elif column in (Col.C, Col.F):
                        self.board[column][row] = Bishop(Color.white if row == 1 else Color.black, location_dict, True)
                    elif column == Col.D:
                        self.board[column][row] = Queen(Color.white if row == 1 else Color.black, location_dict, True)
                    else:
                        self.board[column][row] = King(Color.white if row == 1 else Color.black, location_dict, True)

    def is_empty_location(self, location):
        if self.board[location["col"]][location["row"]] != None:
            return False
        return True

    def is_clear_path(self, old_location, new_location):
        """

        :param old_location:
        :param new_location:
        :return:
        """