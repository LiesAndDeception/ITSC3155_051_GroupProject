from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, default=datetime.utcnow)
    description = Column(String(1000))

    tracking_number = Column(String(50), nullable=True)
    order_status = Column(String(50), nullable=False, default="Processing")
    total_price = Column(DECIMAL(10, 2), nullable=False, default=0.00)

    order_details = relationship("OrderDetail", back_populates="orders")
    payment_information = relationship("PaymentInformation", back_populates="orders")
