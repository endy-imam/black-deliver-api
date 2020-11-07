"""Testing restaurant model
"""

import pytest
from pydantic import ValidationError

from deliver.models import Restaurant


@pytest.fixture
def base_restaurant():
    return {
        'name': "Big Lo's",
        "coordinate": { "latitude": 0, "longitude": 0 },
        'address': '20 W 34th St, New York, NY 10001'
    }


@pytest.mark.parametrize('optionals', [
    {},
    { 'menuUrl': 'https://realpython.com' },
    { 'id': '4974e52b-b6da-4891-a27d-a87bc93c363f' },
])
def test_valid_restaurant_assign(base_restaurant, optionals):
    """Testing valid Restaurant assignment

    Testing if input arguments assign to restaurant correctly
    """
    Restaurant(**base_restaurant, **optionals)


@pytest.mark.parametrize('delete, optionals', [
    (('name',), {}),
    (tuple(), { 'menuUrl': 'realpython.com' }),
    (tuple(), { 'id': 'bad id' }),
])
def test_invalid_restraurant_assign(base_restaurant, delete, optionals):
    """Testing invalid Restaurant assignment

    Testing if input arguments assign output error
    """
    for key in delete:
        del base_restaurant[key]
    with pytest.raises(ValidationError):
        Restaurant(**base_restaurant, **optionals)
    # TODO: Add Additional Testing with Exception Output
