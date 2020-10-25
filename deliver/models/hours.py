"""Classes to define Location

Hierachy of Classes:
- OpeningHours: Object
  - Interval: Object
  - Weekday: IntEnum
"""
from typing import Optional
from datetime import time as Time

from pydantic import BaseModel


class Interval(BaseModel):
    """Class for defining a start to end hours

    Attributes:
        start (Time): The starting time of the day, default 9 AM
        end (Time): The end time of the day, default 5 PM (17:00)
    """
    start: Time = Time(9)
    end: Time = Time(17)


class OpeningHours(BaseModel):
    """Class for defining a start to end hours for the week

    Attributes:
        [Monday, ..., Sunday]: Intervals for each day of the week
    """
    Monday:    Optional[Interval]
    Tuesday:   Optional[Interval]
    Wednesday: Optional[Interval]
    Thursday:  Optional[Interval]
    Friday:    Optional[Interval]
    Saturday:  Optional[Interval]
    Sunday:    Optional[Interval]

    # TODO: Test no-intersection validation

    # TODO: Test current opening w/ timezone difference
