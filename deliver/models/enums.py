"""Module of Enums
"""

from enum import Enum


class ServiceApp(str, Enum):
    """A list of default delivery apps
    """
    UBER_EATS = 'Uber Eats'
    GRUBHUB   = 'Grubhub'
    DOORDASH  = 'Doordash'
    POSTMATES = 'Postmates'
    TOAST     = 'Toast'
    YELP      = 'Yelp'
    CAVIAR    = 'Caviar'
