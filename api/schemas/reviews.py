from pydantic import BaseModel

class ReviewBase(BaseModel):
    customer_id: int
    review_text: str
    score: int

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int

    class Config:
        orm_mode = True
