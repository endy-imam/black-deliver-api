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


# TODO: Maybe add Address Validation

NEITHER_MSG = "Either 'coordinate' and/or 'address' must have a value"
# TODO: Create Location model
class Location(BaseModel):
    """Class for location data, coordinate and/or address

    Attributes (at least one are required):
        coordinate (Coordinate): The exact coordinate of the location
        address (str): A written address
    """
    coordinate: Optional[Coordinate]
    address: Optional[constr(min_length=1)]

    @root_validator
    def at_least_one_required(cls, values):
        """Ensure that there is either a coordinate or address
        """
        if values.get('coordinate') is None and values.get('address') is None:
            raise ValueError(NEITHER_MSG)
        return values
