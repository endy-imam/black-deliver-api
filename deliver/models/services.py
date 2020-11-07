"""Classes to define Services

Hierachy of Classes:
- Services
    - Website
    - Phone
"""

from itertools import chain
from typing import Dict, Optional, Iterator, Union
from pydantic import BaseModel, root_validator, constr, HttpUrl

from .utils import to_lower_camel
from .enums import ServiceApp


SERVICES_BASE_URL = {
    ServiceApp.UBER_EATS: 'https://www.ubereats.com/',
    ServiceApp.GRUBHUB  : 'https://www.grubhub.com/',
    ServiceApp.DOORDASH : 'https://www.doordash.com/stores/',
    ServiceApp.TOAST    : 'https://www.toasttab.com/',
    ServiceApp.YELP     : 'https://yelp.to',
    ServiceApp.POSTMATES: 'https://postmates.com/merchant/',
    ServiceApp.CAVIAR   : 'https://www.trycaviar.com/'
}


class BaseService(BaseModel):
    """A base class for services for phone, website and app

    Attributes:
        pickup:   If service does pickup or takeout
        delivery: If service does delivery
    """
    pickup: bool = False
    delivery: bool = False

    class Config:
        """Config for Restaurant Model

        - Must comply as typical JS/JSON variable name
        """
        alias_generator = to_lower_camel


PHONE_REGEX = (
    r"^[\+]?(1[-\s\.])?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4}$"
)

class PhoneService(BaseService):
    """A class for food services for phone

    Attributes:
        number:   A valid phone number
        pickup:   If service does pickup
        delivery: If service does delivery
    """
    number: constr(regex=PHONE_REGEX)


class OnlineService(BaseService):
    """A class for food services for website or app

    Attributes:
        url:      A link to the app redirect or website
        pickup:   If service does pickup
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

    def has_delivery(self) -> bool:
        """Check if the restaurant has delivery
        """
        return len(self.delivery_apps) > 0 or any(
            service is not None and service.delivery
            for service in self._iter_service()
        )
