from typing import Optional
from pydantic import BaseModel


class OrderDetailBase(BaseModel):
    amount: int
    special_requests: str
    is_delivery: bool


class OrderDetailCreate(OrderDetailBase):
    order_id: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    amount: Optional[int] = None
    special_requests: Optional[str] = None
    is_delivery: Optional[bool] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int

    class ConfigDict:
        from_attributes = True
