"""Testing service models
"""

import pytest
from pydantic import ValidationError

from deliver.models.services import PhoneService, OnlineService, Services


@pytest.mark.parametrize('number', [
    '(123) 456-7890',
    '123) 456-7890',
    '123-456-7890',
    '(123) 4567890',
    '1234567890',
    '+11234567890'
])
def test_valid_phone_assign(number):
    """Testing valid PhoneService assignment
    """
    service_number = PhoneService(number=number)
    assert service_number.number == '(123) 456-7890'


@pytest.mark.parametrize('number', [
    '(123) 456-78900',
    '+123 456-78900',
    '123-4560-7890',
    '1-23456789001',
])
def test_invalid_phone_assign(number):
    """Testing invalid PhoneService assignment
    """
    with pytest.raises(ValidationError):
        PhoneService(number=number)

@pytest.mark.parametrize('pickup, delivery', [
    (False, False), (False, True), (True, True)
])
def test_servicability(pickup, delivery):
    """Testing if services matches availability
    """
    service = Services(
        website=OnlineService(
            url='https://realpython.com',
            pickup=pickup,
            delivery=delivery
        )
    )

    assert service.pickup_available   == pickup
    assert service.delivery_available == delivery
