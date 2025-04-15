from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .drinks import Drink


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    drink_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    drink_id: Optional[int] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    drink: Drink = None

    class ConfigDict:
        from_attributes = True
