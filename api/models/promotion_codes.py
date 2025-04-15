from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from ..dependencies.database import Base

class PromotionCode(Base):
    __tablename__ = "promotion_codes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)  # Optional: allows easy deactivation
