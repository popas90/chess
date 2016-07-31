class InvalidLocationException(Exception):
    pass


COLUMNS = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
ROWS = set(['1', '2', '3', '4', '5', '6', '7', '8'])

    def __init__(self, location_string):
        self._validate_location_string(location_string)
        self._column = location_string[0].lower()
        self._row = location_string[1]

    def __str__(self):
        return self._column + self._row

    def __repr__(self):
        return str(self)

    @property
    def column(self):
        return self._column

    @property
    def row(self):
        return self._row

    def _validate_location_string(self, location_string):
        """
        Throws exceptions if location is not a 2-char string, representing
        a valid chess board location.
        :param location: string representing a board location
        """
        if len(location_string) != 2:
            raise InvalidLocationException(location_string)
        column = location_string[0].lower()
        row = location_string[1]
        if column not in self.COLUMNS:
            raise InvalidLocationException(location_string)
        if row not in self.ROWS:
            raise InvalidLocationException(location_string)
