"""Module of Enums
"""

from enum import Enum


class FoodCategory(str, Enum):
    """A list of type of foods
    """
    pass


class DeliveryApp(str, Enum):
    """A list of default delivery apps
    """
    UBER_EATS = 'Uber Eats'
    GRUBHUB   = 'Grubhub'
    DOORDASH  = 'Doordash'
    POSTMATES = 'Postmates'
    TOAST     = 'Toast'
    YELP      = 'Yelp'


class DiningAmenety(str, Enum):
    """A list of dinimg ameneties
    """
    OUTDOOR_SEATING = "outdoor seating"
    PARKING         = "parking"


class SafetyMeasure(str, Enum):
    """A list of safety measures
    """
    LIMITED_CAPACITY  = "limited capacity"
    SOCIAL_DISTANCING = "social distancing"
    REQUIRING_MASK    = "requiring mask"


class Inclusivity(str, Enum):
    """A list of inclusivity tags
    """
    BIPOC_OWNED    = "BIPOC+ Owned"
    LGBTQ_OWNED    = "LGBTQ+ Owned"
    LGBTQ_FRIENDLY = "LGBTQ+ Friendly"


class WheelchairAccessibity(str, Enum):
    """A list of wheelchair accessibilities
    """
    ENTRANCE = "entrance"
    RESTROOM = "restroom"
    SEATING  = "seating"
    PARKING  = "parking"
    ELEVATOR = "elevator"
