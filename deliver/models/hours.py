"""Classes to define Location

Hierachy of Classes:
- OpeningHours: Object
  - Interval: Object
  - Weekday: IntEnum
"""

from enum import IntEnum

from pydantic import BaseModel


# TODO: Create Interval model
class Interval(BaseModel):
    """TODO: Add Docstring
    """
    pass

# TODO: Create Weekday IntEnum
class Weekday(IntEnum):
    """TODO: Add Docstring
    """
    pass

# TODO: Create OpeningHours model
class OpeningHours(BaseModel):
    """TODO: Add Docstring
    """
    pass
