from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DATETIME, nullable=False, default=datetime.utcnow)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    customer_name = Column(String(100), nullable=False)
    order_number = Column(String(50), nullable=True)
    order_status = Column(String(50), nullable=False, default="Processing")
    total_price = Column(DECIMAL(10, 2), nullable=False, default=0.00)


    order_details = relationship("OrderDetail", back_populates="orders")
    deliveries = relationship("Delivery", back_populates="orders")
    payment_information = relationship("PaymentInformation", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")
