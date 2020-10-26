"""Module of Enums
"""

from enum import Enum

"""
### SERVICES
"""
class DeliveryApp(str, Enum):
    """A list of default delivery apps
    """
    UBER_EATS = 'Uber Eats'
    GRUBHUB   = 'Grubhub'
    DOORDASH  = 'Doordash'
    POSTMATES = 'Postmates'
    TOAST     = 'Toast'
    YELP      = 'Yelp'


SERVICES_BASE_URL = {
    DeliveryApp.UBER_EATS: 'https://www.ubereats.com/',
    DeliveryApp.GRUBHUB  : 'https://www.grubhub.com/',
    DeliveryApp.DOORDASH : 'https://www.doordash.com/stores/',
    DeliveryApp.TOAST    : 'https://www.toasttab.com/',
    DeliveryApp.YELP     : 'https://yelp.to',
    DeliveryApp.POSTMATES: 'https://postmates.com/merchant/'
}
