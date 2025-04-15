from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = "resource_management"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resource_amount = Column(Integer)
    unit = Column(String(50), nullable=False)

    resources = relationship("Resource", back_populates="payment_information")
    # resources already has a relationship to recipes; likely can access the recipes table through that