from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    drink_id = Column(Integer, ForeignKey("drinks.id"))
    amount = Column(Integer, index=True, nullable=False)

    drink = relationship("Drink", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
