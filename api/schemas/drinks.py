from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class DrinkBase(BaseModel):
    drink_name: str
    price: float


class DrinkCreate(DrinkBase):
    pass


class DrinkUpdate(BaseModel):
    drink_name: Optional[str] = None
    price: Optional[float] = None


class Drink(DrinkBase):
    id: int

    class ConfigDict:
        from_attributes = True
