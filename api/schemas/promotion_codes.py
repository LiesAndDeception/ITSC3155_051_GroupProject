from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PromotionCodeBase(BaseModel):
    code: str
    expiration_date: datetime
    is_active: Optional[bool] = True


class PromotionCodeCreate(PromotionCodeBase):
    pass


class PromotionCodeUpdate(BaseModel):
    code: Optional[str] = None
    expiration_date: Optional[datetime] = None
    is_active: Optional[bool] = None


class PromotionCode(PromotionCodeBase):
    id: int

    class ConfigDict:
        from_attributes = True
