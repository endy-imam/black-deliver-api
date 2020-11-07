"""Testing Location and Coordinate model
"""

import pytest
from pydantic import ValidationError

from deliver.models.location import Coordinate



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
