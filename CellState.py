import enum
from enum import Enum

class CellState(enum.Enum):

    uncovered = 'u'
    covered = 'c'
    flagged = 'f'
