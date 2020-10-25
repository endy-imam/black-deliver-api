"""Testing restaurant model
"""

import pytest
from pydantic import ValidationError

from deliver.models import Restaurant


@pytest.mark.parametrize('restaurant_dict', [
    { 'name': "Big Lo's" },
    { 'name': "Lil Pete", 'menuUrl': 'https://realpython.com' },
    { 'name': "Lil Pete", 'id': '4974e52b-b6da-4891-a27d-a87bc93c363f' },
])
def test_valid_restaurant_assign(restaurant_dict):
    """Testing valid Restaurant assignment

    Testing if input arguments assign to restaurant correctly
    """
    Restaurant(**restaurant_dict)
    # TODO: Add Additional Testing with Attributes


@pytest.mark.parametrize('msg, restaurant_dict', [
    (
        'No Name',
        {}
    ),
    (
        'Invalid URL',
        { 'name': "Lil Pete", 'menuUrl': 'https://realpython' },
    ),
    (
        'Bad ID',
        { 'name': "Bad Louie", 'id': 'bad_id' },
    ),
])
def test_invalid_restraurant_assign(msg, restaurant_dict):
    """Testing invalid Restaurant assignment

    Testing if input arguments assign output error
    """
    with pytest.raises(ValidationError):
        Restaurant(**restaurant_dict)
    # TODO: Add Additional Testing with Exception Output


def test_unique_restaurants():
    """Testing unique restaurant

    Testing if unique restaurants have different
    """
    restaurant_dict = { 'name': "Big Lo's" }
    restaurant_a = Restaurant(**restaurant_dict)
    restaurant_b = Restaurant(**restaurant_dict)
    assert restaurant_a.id != restaurant_b.id
