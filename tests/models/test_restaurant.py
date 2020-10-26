"""Testing restaurant model
"""

import pytest
from pydantic import ValidationError

from deliver.models import Restaurant


@pytest.fixture
def base_restaurant():
    return {
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
def test_valid_restaurant_assign(base_restaurant, optionals):
    """Testing valid Restaurant assignment

    Testing if input arguments assign to restaurant correctly
    """
    Restaurant(**base_restaurant, **optionals)


@pytest.mark.parametrize('delete, optionals', [
    (('name',), {}),
    (('location',), {}),
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


def test_unique_restaurants(base_restaurant):
    """Testing unique restaurant

    Testing if unique restaurants have different
    """
    restaurant_a = Restaurant(**base_restaurant)
    restaurant_b = Restaurant(**base_restaurant)
    assert restaurant_a.id != restaurant_b.id
