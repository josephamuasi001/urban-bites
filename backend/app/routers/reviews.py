from fastapi import APIRouter, Depends

from app.auth.auth_bearer import get_current_user

from app.schemas.review import (
    ReviewCreate,
    ReviewUpdate
)

from app.services.review_service import (
    create_review,
    get_restaurant_reviews,
    get_review_by_id,
    update_review,
    delete_review
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


@router.get("/item/{review_id}")
def get_review(review_id: str):

    return get_review_by_id(
        review_id
    )
    

@router.put("/{review_id}")
def edit_review(
    review_id: str,
    review: ReviewUpdate
):

    return update_review(
        review_id,
        review
    )
    


@router.delete("/{review_id}")
def remove_review(review_id: str):

    return delete_review(
        review_id
    )

