from pydantic import BaseModel
from typing import Optional


class DeliveryBase(BaseModel):
    customer_name: str
    order_number: str
    phone_number: int
    email: str
    order_delivery_status: str


class DeliveryCreate(DeliveryBase):
    order_id: int


class DeliveryUpdate(BaseModel):
    customer_name: Optional[str] = None
    order_number: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    order_delivery_status: Optional[str] = None


class Delivery(DeliveryBase):
    id: int
    order_id: int


    class ConfigDict:
        from_attributes = True




class DeliveryStatusOutForDelivery(BaseModel):
    order_delivery_status: Optional[str] = "Out For Delivery"


class DeliveryStatusDelivered(BaseModel):
    order_delivery_status: Optional[str] = "Delivered"