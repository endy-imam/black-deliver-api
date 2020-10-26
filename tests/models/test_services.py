"""Testing services model
"""

import pytest

from deliver.models.services import Services
from deliver.models.enums    import DeliveryApp


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
        },
    }


def test_valid_restaurant_assign(base_services):
    """Testing valid Restaurant assignment

    Testing if input arguments assign to restaurant correctly
    """
    Services(**base_services)
