from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .drinks import Drinks


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
    drink_id: int
    resource_id: int

class RecipeUpdate(BaseModel):
    drink_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    drink: Drink = None
    resource: Resource = None

    class ConfigDict:
        from_attributes = True
