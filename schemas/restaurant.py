from typing import Optional
from pydantic import BaseModel, ConfigDict

class RestaurantBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    rating: int
    name: str
    site: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    lat: float
    lng: float

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(RestaurantBase):
    id: Optional[str] = None

class Restaurant(RestaurantBase):
    id: str