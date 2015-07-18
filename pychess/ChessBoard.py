from pychess.Pawn import Pawn
from pychess.Rook import Rook
from pychess.Bishop import Bishop
from pychess.Knight import Knight
from pychess.Queen import Queen
from pychess.King import King
from pychess.Piece import *

## TODO create a persistence schema for loading a predefined config
## TODO use persistence for loading initial config

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


class ChessBoard:

    def __init__(self):
        """

        :return:
        """
        self._reset_board()

    def _reset_board(self):
        """
        Brings the board to the initial state, with all pieces at starting positions.
        """
        rows, columns = range(1, 9), "ABCDEFGH"
        self._board = [{col: None for col in columns} for _ in rows]

        for column in Col:
            for row in range(1, 8):
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

    def _set_piece(self, piece, row, column):

    def is_empty_location(self, location):
        """

        :param location:
        :return:
        """
        if self.board[location["col"]][location["row"]] != None:
            return False
        return True

    def is_clear_path(self, old_location, new_location):
        """

        :param old_location:
        :param new_location:
        :return:
        """