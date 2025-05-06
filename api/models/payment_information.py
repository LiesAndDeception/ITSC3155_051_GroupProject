from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = "payment_information"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    card_information = Column(Integer)
    transaction_status = Column(String(50), nullable=False)
    transaction_type = Column(String(50), nullable=False)

    orders = relationship("Order", back_populates="payment_information")