# TODO make this stateful, with a reference to the unique Board in the game
# TODO both this and Board should be singletons
from model.Piece import Color
from model.LocationValidator import is_valid_location_string


COL_INT = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
COL_STR = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
col_row_range = range(1, 9)


def generate_all_moves(piece, location):
    all_locations = set()
    color_adjustment = 1 if piece.color == Color.White else -1
    for direction in piece.directions:
        primitive_moves = list(direction[0])
        new_location = generate_move(location, primitive_moves,
                                     color_adjustment)
        if new_location is not None:
            all_locations.add(new_location)
    return all_locations


def generate_move(location, primitive_moves, color_adjustment):
    col_index = COL_INT[location[0]]
    row_index = int(location[1])
    for primitive in primitive_moves:
        if primitive == 'F':
            row_index = row_index + color_adjustment
        elif primitive == 'B':
            row_index = row_index - color_adjustment
        elif primitive == 'R':
            col_index = col_index + color_adjustment
        elif primitive == 'L':
            col_index = col_index - color_adjustment
    if row_index not in col_row_range or col_index not in col_row_range:
        return None
    new_location = str(COL_STR[col_index]) + str(row_index)
    if is_valid_location_string(new_location):
        return new_location
    return None
