"""Testing Location and Coordinate model
"""

import pytest
from pydantic import ValidationError

from deliver.models.location import Coordinate, Location, NEITHER_MSG



@pytest.mark.parametrize('latitude' , [- 90, 0,  90])
@pytest.mark.parametrize('longitude', [-180, 0, 180])
def test_valid_coordinate_assignments(latitude, longitude):
    """Testing valid Coordinate assignment

    Testing if input arguments assign to coordinate correctly
    """
    Coordinate(latitude=latitude, longitude=longitude)


@pytest.mark.parametrize('latitude' , [-100, 0, 100])
@pytest.mark.parametrize('longitude', [-200, 0, 200])
def test_invalid_coordinate_assignment(latitude, longitude):
    """Testing invalid Coordinate assignment

    Testing if input arguments assign to out of bound
    """
    if latitude != 0 and longitude != 0:
        with pytest.raises(ValidationError):
            Coordinate(latitude=latitude, longitude=longitude)



def test_valid_location_assignment():
    """Testing valid Location assignment

    Testing that at least one of those fields are accepted
    """
    coordinate = Coordinate()
    address = '20 W 34th St, New York, NY 10001'
    Location(address=address)
    Location(coordinate=coordinate)
    Location(coordinate=coordinate, address=address)


def test_invalid_location_assignment_none():
    """Testing invalid Location assignment w/ no arguments

    Testing if it neither have coordinate or address output a
    ValidationError
    """
    with pytest.raises(ValidationError) as excval:
        Location()


def test_invalid_location_assignment_address():
    """Testing invalid Location assignment w/ empty address

    Testing if an empty address string returns a ValidationError
    """
    with pytest.raises(ValidationError):
        Location(address='')
