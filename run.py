from model.Piece import Color
from model.Pawn import Pawn
from model.MovesGenerator import generate_all_moves

generate_all_moves(Pawn(Color.White), 'd2')
