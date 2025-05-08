from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    order_id = Column(Integer, ForeignKey("orders.id"))
    customer_name = Column(String(100), nullable=False)
    order_number = Column(String(50), nullable=True)
    phone_number = Column(Integer, nullable=False)
    email = Column(String(75), nullable=False)
    order_delivery_status = Column(String(50), nullable=False, default="Not Delivered")


    orders = relationship("Order", back_populates="deliveries")
