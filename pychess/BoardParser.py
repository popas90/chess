from pychess.Piece import *
from pychess.Pawn import Pawn
from pychess.Rook import Rook
from pychess.Bishop import Bishop
from pychess.Knight import Knight
from pychess.Queen import Queen
from pychess.King import King


class BoardParser:
    """
    Used for parsing the text file containing board configurations.
    """

    @staticmethod
    def read_board_from_file(file_path):
        """
        Parses the persistence file and returns a tuple of board configuration and next-to-move.
        :param file_path: path to the persistence file
        :return: board configuration as dict
        """
        rows, columns = range(1, 10), "ABCDEFGH"
        board = [{col: None for col in columns} for _ in rows]
        next_to_move = None
        try:
            with open(file_path, "r") as file:
                first_line = file.readline().strip()
                next_to_move = BoardParser._get_color_from_symbol(first_line)
                row_iter = iter(rows)
                for line in file:
                    column_iter = iter(columns)
                    row = next(row_iter)
                    symbols = line.split(" ")
                    for sym in symbols:
                        col = next(column_iter)
                        board[row][col] = BoardParser._get_piece_from_token(sym.rstrip(), row, col)
        except ParsingError as err:
            print("An error occurred while parsing the board from file : {0}".format(err))

        return next_to_move, board

    @staticmethod
    def _get_piece_from_token(token, row, col):
        """
        Returns a new Piece object from the two-letter symbol parameter.
        :param token: string representing piece and color
        :param row: row location
        :param col: column location
        :return: a new Piece object or None
        """
        if len(token) != 2:
            raise ParsingError("Parsing error: Tokens should contain two characters only: {0}:{1}"
                               .format(token, len(token)))

        color = BoardParser._get_color_from_symbol(token[1])

        piece = token[0].capitalize()
        if piece == "K":
            return King(color, (row, col))
        elif piece == "Q":
            return Queen(color, (row, col), True)
        elif piece == "R":
            return Rook(color, (row, col), True)
        elif piece == "B":
            return Bishop(color, (row, col), True)
        elif piece == "N":
            return Knight(color, (row, col), True)
        elif piece == "P":
            return Pawn(color, (row, col), True)
        elif piece == "0":
            return None
        else:
            raise ParsingError("Parsing error: Unrecognized piece")

    @staticmethod
    def _get_color_from_symbol(sym):
        """
        Returns a Color member, based on the symbol parameter.
        :param sym: character representing the color
        :return: a Color member
        """

        if len(sym) != 1:
            raise ParsingError("Parsing error: Symbols should contain one character only: {0}:{1}"
                               .format(sym, len(sym)))

        if sym.capitalize() == "W":
            color = Color.white
        elif sym.capitalize() == "B":
            color = Color.black
        else:
            raise ParsingError("Parsing error: Color should be white (W) or black (B)")
        return color


class ParsingError(Exception):
    """
    Defines a ParsingError type of exception.
    """

    def __init__(self, message):
        super(ParsingError, self).__init__(message)
