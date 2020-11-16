"""Testing restaurant model
"""

import pytest
from pydantic import ValidationError

from deliver.models import Restaurant
from deliver.models.services import Services, OnlineService


@pytest.fixture
def base_restaurant():
    """Base fixture of a minimal restaurant
    """
    return {
    	'name': "Mai's Coffee House",
        'coordinate': {
    	    'latitude': 42.35,
    	    'longitude': -71.05
        }
    }

def _mock_service(pickup, delivery):
    """Mock fixture for pickup and delivery for services
    """
    return Services(
        website=OnlineService(
            url='https://realpython.com',
            pickup=pickup,
            delivery=delivery
        )
    )


@pytest.mark.parametrize('optionals', [
    {},
    { 'menuUrl': 'https://realpython.com' },
    { 'id': '4974e52b-b6da-4891-a27d-a87bc93c363f' },
    { 'foodCategories': ['Coffee', 'Cafe', 'Drinks'] },
    { 'address': '212 Washington St, Boston, MA 02108' },
])
def test_valid_restaurant_assign(base_restaurant, optionals):
    """Testing valid Restaurant assignment

    Testing if input arguments assign to restaurant correctly
    """
    Restaurant(**base_restaurant, **optionals)


@pytest.mark.parametrize('pickup, delivery', [
    (False, False), (False, True), (True, True)
])
def test_servicability(base_restaurant, pickup, delivery):
    """Validate availability from services to entire restaurant model
    """
    services = _mock_service(pickup, delivery)
    restaurant = Restaurant(**base_restaurant, services=services)
    assert restaurant.pickup_available   == pickup
    assert restaurant.delivery_available == delivery


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

@pytest.fixture
def dynamo_example():
    """Full example of a restaurant model in DynamoDB
    """
    return {
        "id": "4e935397-848c-488b-b3e2-bb933b5c2064",
        "name": "Felix BBQ with Soul",
        "latitude": 33.20989,
        "longitude": -117.31234,
        "address": "3616 Ocean Ranch Blvd, Oceanside, CA 92056",
        "menuUrl": "https://www.felixsbbq.com/",
        "pickupAvailable": True,
        "deliveryAvailable": True,
        "services": {
            "website": {
                "url": "https://www.felixsbbq.com/",
                "pickup": True,
                "delivery": True
            },
            "apps": {
                "Grubhub": {
                    "url": "https://www.grubhub.com/",
                    "pickup": True,
                    "delivery": True
                },
                "Doordash": {
                    "url": "https://www.doordash.com/",
                    "pickup": True,
                    "delivery": True
                },
                "Postmates": {
                    "url": "https://postmates.com/merchant/",
                    "pickup": True,
                    "delivery": True
                }
            }
        }
    }

def test_dynamo_convert(dynamo_example):
    """Test consistent conversion for dynamodb
    """
    obj1 = Restaurant.from_dynamo(dynamo_example)
    obj2 = Restaurant.from_dynamo(obj1.to_dynamo())
    assert obj1 == obj2
