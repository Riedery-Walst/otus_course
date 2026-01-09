from typing import Optional
from pydantic import BaseModel, HttpUrl

from models.brewery_type import BreweryType


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: BreweryType

    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]

    city: str
    state_province: str
    postal_code: str
    country: str

    longitude: Optional[float]
    latitude: Optional[float]

    phone: Optional[str]
    website_url: Optional[HttpUrl]

    state: Optional[str]
    street: Optional[str]
