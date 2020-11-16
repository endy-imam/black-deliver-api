"""Classes to define Location

Hierachy of Classes:
- Location: Object
  - Coordinate: Object
  - Address: str
"""

from pydantic import BaseModel, condecimal


class Coordinate(BaseModel):
    """Class for coordinates on earth

    Attributes:
        latitude (Decimal): The latitude of the coordinate
        longitude (Decimal): The longitude of the coordinate
    """
    latitude:  condecimal(ge=- 90, le= 90) = 0
    longitude: condecimal(ge=-180, le=180) = 0
