from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Sandwich(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drink_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    recipes = relationship("Recipe", back_populates="drink")
    order_details = relationship("OrderDetail", back_populates="drink")
