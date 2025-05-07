from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    order_id = Column(Integer, ForeignKey("orders.id"))
    amount = Column(Integer, index=True, nullable=False)
    special_requests = Column(String(1000), nullable=True)
    is_delivery = Column(Boolean, nullable=False)


    orders = relationship("Order", back_populates="order_details")