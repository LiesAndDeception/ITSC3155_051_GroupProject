from pydantic import BaseModel
from typing import Optional


class MenuItemBase(BaseModel):
    dish_name: str
    ingredients: Optional[str] = None
    price: float
    calories: Optional[int] = None
    drink_category: Optional[str] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    dish_name: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    drink_category: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
