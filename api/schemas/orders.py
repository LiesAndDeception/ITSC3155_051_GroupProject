from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_name: str
    order_number: Optional[str] = None
    order_status: Optional[str] = "Processing"
    total_price: Optional[float] = 0.00


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    order_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail]
    
    class ConfigDict:
        from_attributes = True
