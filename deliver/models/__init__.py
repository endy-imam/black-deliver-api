"""Classes to define Restaurant Info

Hierachy of Classes:
- Restaurant Info: Object
    - Unique Id: UUID
    - Restaurant Name: str
    - Location: Object
        - Coordinate: Object
        - Address: Object
    - OpeningHours: Object
    - Food Categories: Optional[Set[str]]
    - MenuURL: Optional[HttpUrl]
    - Services: List[str]                  # TODO: Figure out generate
    - Safety Measures: List[str]
    - Dining Ameneties: List[str]
    - Delivery Services: Object
    - Inclusive Tags: List[str]
    - Wheelchair Accessibity: List[str]
"""

from typing import Optional, Set, Dict, Union, Any, Type
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, HttpUrl, conset, root_validator

from .utils    import to_lower_camel
from .location import Location
from .hours    import OpeningHours
from .services import Services
from .enums    import (
    FoodCategory,
    DiningAmenety,
    SafetyMeasure,
    Inclusivity,
    WheelchairAccessibity
)


class Restaurant(BaseModel):
    """Class for full restaurant info with validation

    Attributes:
        id (UUID): Unique UUID generated by default
        name (str): Restaurant Name
        location (Location):
            Data containing coordinate + address
        opening_hours (OpeningHours):
            A list of hours in the week for available services
        food_category (Set[FoodCategory]):
            A set of type of food, should be non-empty
        dining_available (bool):
            If the restaurant is available for dining
        dining_ameneties (Optional[Set[DiningAmenety]]):
            A set of ameneties, optional but only if dining
        safety_measures (Optional[Set[SafetyMeasure]]):
            A set of safety measures, required if dining available right now
        services (Services):
            A list of pickup and deliver services available
        inclusivities (Set[Inclusivity]):
            A set of inclusivity tags
        wheelchair_accessibilities (Set[WheelchairAccessibity]):
            A set of wheelchair accessibilities
    """
    id: UUID = Field(default_factory=uuid4)
    name: str
    location: Location
    opening_hours: OpeningHours = OpeningHours()
    food_categories: Set[Union[FoodCategory, str]] = set()
    menu_url: Optional[HttpUrl]
    dining_available: bool = False
    pickup_available: bool = False
    curbside_available: bool = False
    delivery_available: bool = False
    dining_ameneties: Optional[Set[DiningAmenety]]
    safety_measures: Optional[Set[SafetyMeasure]]
    services: Services = Services()
    inclusivities: Set[Inclusivity] = set()
    wheelchair_accessibities: Set[WheelchairAccessibity] = set()


    class Config:
        """Config for Restaurant Model

        - Must comply as typical JS/JSON variable name
        """
        alias_generator = to_lower_camel

    @root_validator
    def has_pickup(cls, values):
        """Check if the restaurant has pickup
        """
        services = values['services']
        values['pickup_available'] = (
            services.has_pickup() if services else False
        )
        values['curbside_available'] = (
            services.has_curbside() if services else False
        )
        values['delivery_available'] = (
            services.has_delivery() if services else False
        )
        return values
