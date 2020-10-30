"""Testing services model
"""

import pytest
from pydantic import ValidationError

from deliver.models.services import BaseService, Services
from deliver.models.enums    import DeliveryApp


@pytest.mark.parametrize('pickup, curbside, delivery', (
    (True , False, False),
    (True , True , False),
    (False, False, True ),
    (True , False, True ),
    (True , True , True ),
))
def test_valid_service_assign(pickup, curbside, delivery):
    """Test that all cases are valid services
    """
    BaseService(pickup=pickup, curbside=curbside, delivery=delivery)

def test_invalid_service_no_services():
    """Test that it returns exception when no service output available
    """
    with pytest.raises(ValidationError):
        BaseService()

def test_invalid_service_curbside_no_pickup():
    """Test that it returns exception when curbside without pickup
    """
    with pytest.raises(ValidationError):
        BaseService(curbside=True)


@pytest.fixture
def base_services():
    """The default data model for services
    """
    return {
        'website': {
            'url': 'https://www.cnrguys.com/',
            'pickup': True,
            'curbside': True,
        },
        'phone': {
            'number': '999-999-9999',
            'pickup': True,
        },
        'deliveryApps': {
            DeliveryApp.UBER_EATS: 'https://www.ubereats.com/',
            DeliveryApp.GRUBHUB  : 'https://www.grubhub.com/',
            DeliveryApp.DOORDASH : 'https://www.doordash.com/stores/',
            DeliveryApp.TOAST    : 'https://www.toasttab.com/',
            DeliveryApp.YELP     : 'https://yelp.to',
        },
        'extras': {
            'Proprietary': {
                'url': 'https://order.cloverfoodlab.com/order',
                'pickup': True,
            },
            DeliveryApp.POSTMATES: {
                'url': 'https://postmates.com/merchant/',
                'pickup': True,
                'delivery': True
            },
            DeliveryApp.CAVIAR: {
                'url': 'https://www.trycaviar.com/store/dig-boston-915050/en-US',
                'pickup': True,
                'delivery': True
            },
        },
    }


def test_valid_restaurant_assign(base_services):
    """Testing valid Restaurant assignment

    Testing if input arguments assign to restaurant correctly
    """
    Services(**base_services)

def test_services_availability(base_services):
    """Testing services returns existing service

    Testing if base_service can see if it can do pickup, curbside,
    and delivery.
    """
    services = Services(**base_services)
    assert services.has_pickup()
    assert services.has_curbside()
    assert services.has_delivery()


def test_services_no_availability(base_services):
    """Testing services returns existing service

    Testing if base_service can see if it can do pickup, curbside,
    and delivery.
    """
    services = Services()
    assert not services.has_pickup()
    assert not services.has_curbside()
    assert not services.has_delivery()
