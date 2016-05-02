class Board:

    def __init__(self):
        self._state = ['RNBKQBNR',
                       'PPPPPPPP',
                       '........',
                       '........',
                       '........',
                       '........',
                       'pppppppp',
                       'rnbkqbnr']

    def is_free_location(self, location):
        pass

    def get_piece_from_location(self, location):
        return self._state[location[0]][location[1]]
