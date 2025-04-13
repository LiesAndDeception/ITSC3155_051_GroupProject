from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    review_text = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
