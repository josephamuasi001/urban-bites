from fastapi import APIRouter

from app.schemas.restaurant import RestaurantCreate
from app.services.restaurant_service import create_restaurant

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)


@router.post("/")
def add_restaurant(restaurant: RestaurantCreate):
    return create_restaurant(restaurant)