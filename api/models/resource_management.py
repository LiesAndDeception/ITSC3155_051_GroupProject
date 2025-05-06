from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class ResourceManagement(Base):
    __tablename__ = "resource_management"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resource_id = Column(Integer, ForeignKey("resources.id"))
    resource_amount = Column(Integer)
    unit = Column(String(50), nullable=False)

    resources = relationship("Resource", back_populates="resource_management")
    # resources already has a relationship to recipes; likely can access the recipes table through that