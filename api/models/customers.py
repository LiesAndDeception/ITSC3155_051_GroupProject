from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(500), unique=True, nullable=False)
    phone = Column(String(25), nullable=False)
    address = Column(String(500), nullable=True)

    orders = relationship("Order", back_populates="customer")
