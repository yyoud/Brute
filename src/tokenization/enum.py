from enum import Enum as _Enum

class TokenTypes(_Enum):
    """

    """
    m = _Enum(1, "m", "_T")
    MAJUSCULE_CHAR = 1
    MINISCULE_CHAR = 2
    DIGIT = 3
    SYMBOL = 4
    PRESET = 4 # includes all preset tokens.
    CHAR_SEQUENCE = 5
    DIGIT_SEQUENCE = 5
    SYMBOL_SEQUENCE = 6
    MIXED_SEQUENCE = 7
