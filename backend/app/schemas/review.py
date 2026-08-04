from pydantic import BaseModel


class ReviewCreate(BaseModel):
    restaurant_id: str
    rating: int
    comment: str