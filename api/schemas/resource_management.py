from typing import Optional
from pydantic import BaseModel



class ResourceManagementBase(BaseModel):
    resource_amount = int
    unit = str


class ResourceManagementCreate(ResourceManagementBase):
    pass


class ResourceManagementUpdate(BaseModel):
    resource_amount: Optional[int] = None
    unit: Optional[str] = None


class ResourceManagement(ResourceManagementBase):
    id: int


    class ConfigDict:
        from_attributes = True