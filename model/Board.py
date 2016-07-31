from model.Location import Location


class Board:

    SQUARES = [str(col + row)
               for col in Location.COLUMNS
               for row in Location.ROWS]

    def __init__(self):
        self._state = {n: None for n in Board.SQUARES}

    def __getitem__(self, location_string):
        return self._state[Location(location_string)]

    def _populate_with_default(self):
        pass

    def is_location_empty(self, location):
        return True if self.get_piece(location) == '.' else False

    def get_piece(self, location):
        return self._state[location[0]][location[1]]
