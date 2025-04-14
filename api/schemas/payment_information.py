from typing import Optional
from pydantic import BaseModel



class PaymentInformationBase(BaseModel):
    card_information = int
    transaction_status = str
    transaction_type = str


class PaymentInformationCreate(PaymentInformationBase):
    pass


class PaymentInformationUpdate(BaseModel):
    card_information: Optional[int] = None
    transaction_status: Optional[str] = None
    transaction_type: Optional[str] = None


class PaymentInformation(PaymentInformationBase):
    id: int


    class ConfigDict:
        from_attributes = True