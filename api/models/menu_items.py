from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(100), nullable=False)
    ingredients = Column(String(500), nullable=True)
    price = Column(DECIMAL(5, 2), nullable=False, default=0.00)
    calories = Column(Integer, nullable=True)
    drink_category = Column(String(100), nullable=True)  # e.g., 'coffee', 'tea', or None
