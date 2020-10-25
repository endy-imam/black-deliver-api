"""Testing restaurant model
"""

import pytest
from pydantic import ValidationError

from deliver.models import Restaurant


_base_restaurant = {
        'name': "Big Lo's",
        'location': {
            'address': '20 W 34th St, New York, NY 10001'
        }
    }


@pytest.mark.parametrize('optionals', [
    {},
    { 'menuUrl': 'https://realpython.com' },
    { 'id': '4974e52b-b6da-4891-a27d-a87bc93c363f' },
])
def test_valid_restaurant_assign(optionals):
    """Testing valid Restaurant assignment

    Testing if input arguments assign to restaurant correctly
    """
    Restaurant(**_base_restaurant, **optionals)


@pytest.mark.parametrize('data', [
    { 'location': _base_restaurant['location'] },
    { 'name': "Big Lo's" },
    { **_base_restaurant, 'menuUrl': 'realpython.com' },
    { **_base_restaurant, 'id': 'bad id' },
])
def test_invalid_restraurant_assign(data):
    """Testing invalid Restaurant assignment

    Testing if input arguments assign output error
    """
    with pytest.raises(ValidationError):
        Restaurant(**data)
    # TODO: Add Additional Testing with Exception Output


def test_unique_restaurants():
    """Testing unique restaurant

    Testing if unique restaurants have different
    """
    restaurant_a = Restaurant(**_base_restaurant)
    restaurant_b = Restaurant(**_base_restaurant)
    assert restaurant_a.id != restaurant_b.id
