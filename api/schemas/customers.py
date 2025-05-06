from pydantic import BaseModel, EmailStr

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str | None = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
