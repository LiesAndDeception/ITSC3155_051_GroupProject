from pydantic import BaseModel
from typing import Optional

class PaymentInformationBase(BaseModel):
    order_id: int
    payment_method: str
    card_information: Optional[int] = None
    transaction_status: str
    transaction_type: str
    amount: float

    class Config:
        orm_mode = True

class PaymentInformationCreate(PaymentInformationBase):
    pass

class PaymentInformationUpdate(PaymentInformationBase):
    pass

class PaymentInformation(PaymentInformationBase):
    id: int

    class Config:
        orm_mode = True
