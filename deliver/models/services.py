"""Classes to define Services

Hierachy of Classes:
- Services
    - Website
    - Phone
"""

from itertools import chain
from typing import Dict, Optional, Iterator
from pydantic import BaseModel, root_validator, constr, HttpUrl

from .utils import to_lower_camel
from .enums import DeliveryApp


SERVICES_BASE_URL = {
    DeliveryApp.UBER_EATS: 'https://www.ubereats.com/',
    DeliveryApp.GRUBHUB  : 'https://www.grubhub.com/',
    DeliveryApp.DOORDASH : 'https://www.doordash.com/stores/',
    DeliveryApp.TOAST    : 'https://www.toasttab.com/',
    DeliveryApp.YELP     : 'https://yelp.to',
    DeliveryApp.POSTMATES: 'https://postmates.com/merchant/',
    DeliveryApp.CAVIAR   : 'https://www.trycaviar.com/'
}


class BaseService(BaseModel):
    """A base class for services for phone, website and app

    Attributes:
        pickup:   If service does pickup or takeout
        curbside: If service does curbside pickup only if pickup
        delivery: If service does delivery
    """
    pickup: bool = False
    curbside: bool = False
    delivery: bool = False

    class Config:
        """Config for Restaurant Model

        - Must comply as typical JS/JSON variable name
        """
        alias_generator = to_lower_camel

    @root_validator
    def curbside_when_pickup(cls, values):
        """Validate that curbside is only when pickup is available
        """
        curbside = values.get('curbside', False)
        pickup   = values.get('pickup', False)
        if curbside and not pickup:
            raise ValueError("Curbside only available if pickup is available")
        return values

    @root_validator
    def has_delivery_output(cls, values):
        """Validate that it has such service available
        """
        fields = ('pickup', 'curbside', 'delivery')
        if not any(values.get(field, False) for field in fields):
            raise ValueError("Valid service if it has pickup or delivery")
        return values


PHONE_REGEX = (
    r"^[\+]?(1[-\s\.])?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4}$"
)

class PhoneService(BaseService):
    """A class for food services for phone

    Attributes:
        number:   A valid phone number
        pickup:   If service does pickup
        curbside: If service does curbside pickup only if pickup
        delivery: If service does delivery
    """
    number: constr(regex=PHONE_REGEX)


class OnlineService(BaseService):
    """A class for food services for website or app

    Attributes:
        url:      A link to the app redirect or website
        pickup:   If service does pickup
        curbside: If service does curbside pickup only if pickup
        delivery: If service does delivery
    """
    url: HttpUrl


class Services(BaseModel):
    """A class for collections of food services

    Attributes:
        website Food service via restaurant's own site
        phone: Food service via phone number
        delivery_apps: A list of links to delivery-only app services
        extras: A list of extra online/app services
    """
    website: Optional[OnlineService]
    phone: Optional[PhoneService]
    delivery_apps: Dict[str, HttpUrl] = {}
    extras: Dict[str, OnlineService] = {}

    class Config:
        """Config for Restaurant Model

        - Must comply as typical JS/JSON variable name
        """
        alias_generator = to_lower_camel

    def _iter_service(self) -> Iterator[BaseService]:
        """An iterator of services outside of delivery_apps
        """
        return filter(
            lambda service: service is not None,
            chain((self.website, self.phone), self.extras.values())
        )

    def has_pickup(self) -> bool:
        """Check if the restaurant has pickup
        """
        return any(
            service is not None and service.pickup
            for service in self._iter_service()
        )

    def has_curbside(self) -> bool:
        """Check if the restaurant has curbside pickup
        """
        return any(
            service is not None and service.curbside
            for service in self._iter_service()
        )

    def has_delivery(self) -> bool:
        """Check if the restaurant has delivery
        """
        return len(self.delivery_apps) > 0 or any(
            service is not None and service.delivery
            for service in self._iter_service()
        )
