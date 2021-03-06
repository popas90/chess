class InvalidLocationException(Exception):
    pass


COLUMNS = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
ROWS = set(['1', '2', '3', '4', '5', '6', '7', '8'])


def validate_location_string(location_string):
    """
    Throws exceptions if location is not a 2-char string, representing
    a valid chess board location.
    :param location: string representing a board location
    """
    if not is_valid_location_string(location_string):
        raise InvalidLocationException()


def is_valid_location_string(location_string):
    if len(location_string) != 2:
        return False
    column = location_string[0].lower()
    row = location_string[1]
    if column not in COLUMNS:
        return False
    if row not in ROWS:
        return False
    return True
