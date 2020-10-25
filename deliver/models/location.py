"""Classes to define Location

Hierachy of Classes:
- Location: Object
  - Coordinate: Object
  - Address: str
"""

from pydantic import BaseModel, confloat


class Coordinate(BaseModel):
    """Class for coordinates on earth

    Attributes:
        latitude (float): The latitude of the coordinate
        longitude (float): The longitude of the coordinate
    """
    latitude:  confloat(ge=- 90, le= 90)
    longitude: confloat(ge=-180, le=180)


# TODO: Create Location model
class Location(BaseModel):
    """TODO: Add Docstring
    """
    pass
