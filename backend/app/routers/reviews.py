from fastapi import APIRouter, Depends

from app.auth.auth_bearer import get_current_user
from app.schemas.review import ReviewCreate
from app.services.review_service import (
    create_review,
    get_restaurant_reviews
)

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post("/")
def add_review(
    review: ReviewCreate,
    current_user=Depends(get_current_user)
):

    return create_review(
        review,
        current_user["sub"]
    )


@router.get("/{restaurant_id}")
def get_reviews(restaurant_id: str):

    return get_restaurant_reviews(
        restaurant_id
    )