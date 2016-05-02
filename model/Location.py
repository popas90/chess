class InvalidLocationException(Exception):
    pass


class Location:
    """
    Class representing a board location.
    """

    COLUMNS = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    ROWS = set(['1', '2', '3', '4', '5', '6', '7', '8'])
    COL_INT = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    def __init__(self, location_string):
        self.validate_location_string(location_string)
        self._column, self._row = self._extract_coordinates(location_string)

    def _extract_coordinates(self, location):
        return (Location.COL_INT[location[0]], int(location[1]))

    def validate_location_string(self, location):
        """
        Throws exceptions if location is not a 2-char string, representing
        a valid chess board location.
        :param location: string representing a board location
        """
        if len(location) != 2:
            raise InvalidLocationException(location)
        column = location[0]
        row = location[1]
        if column not in self.COLUMNS:
            raise InvalidLocationException(location)
        if row not in self.ROWS:
            raise InvalidLocationException(location)
