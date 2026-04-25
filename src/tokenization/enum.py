from enum import Enum as _Enum

class TokenTypes(_Enum):
    """
    Global enumeration for all token types are here.
    """
    PRESET = 1 # includes all preset tokens.
    MAJUSCULE_CHAR = 2
    MINISCULE_CHAR = 3
    DIGIT = 4
    PUNCTUATION = 5

    PRESET_REP = 1
    MAJ_CHAR_REP = 2
    MIN_CHAR_REP = 3
    DIGIT_REP = 4
    PUNCTUATION_REP = 5

    # 1a231a231a23 -> (1a23:3) t: 8, H=0
    # 1q1q1q1a231a231a231a23 -> (1q:3) t=8,(1a23:4) t:8, H=0
    # this isnt right
    MIXED_SEQUENCE = 8
