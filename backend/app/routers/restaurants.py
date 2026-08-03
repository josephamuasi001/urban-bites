from fastapi import APIRouter

from app.schemas.restaurant import RestaurantCreate

from app.services.restaurant_service import (
    create_restaurant,
    get_all_restaurants,
    get_restaurant_by_id
)

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)


@router.get("/")
def get_restaurants():
    return get_all_restaurants()


@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: str):
    return get_restaurant_by_id(restaurant_id)


@router.post("/")
def add_restaurant(restaurant: RestaurantCreate):
    return create_restaurant(restaurant)