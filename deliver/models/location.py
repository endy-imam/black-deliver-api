"""Classes to define Location

Hierachy of Classes:
- Location: Object
  - Coordinate: Object
  - Address: str
"""

from typing import Optional

from pydantic import BaseModel, confloat, constr, root_validator


class Coordinate(BaseModel):
    """Class for coordinates on earth

    Attributes:
        latitude (float): The latitude of the coordinate
        longitude (float): The longitude of the coordinate
    """
    latitude:  confloat(ge=- 90, le= 90) = 0
    longitude: confloat(ge=-180, le=180) = 0
