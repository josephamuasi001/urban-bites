from fastapi import APIRouter

from app.schemas.menu import MenuItemCreate
from app.services.menu_service import (
    create_menu_item,
    get_all_menu_items,
    get_menu_items_by_restaurant
)

router = APIRouter(
    prefix="/menus",
    tags=["Menus"]
)


@router.post("/")
def create(menu_item: MenuItemCreate):
    return create_menu_item(menu_item)


@router.get("/")
def get_all():
    return get_all_menu_items()


@router.get("/{restaurant_id}")
def get_by_restaurant(restaurant_id: str):
    return get_menu_items_by_restaurant(restaurant_id)