from fastapi import APIRouter

from app.schemas.menu import (
    MenuItemCreate,
    MenuItemUpdate
)

from app.services.menu_service import (
    create_menu_item,
    get_all_menu_items,
    get_menu_items_by_restaurant,
    get_menu_item_by_id,
    update_menu_item,
    delete_menu_item
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


@router.get("/item/{menu_item_id}")
def get_by_id(menu_item_id: str):
    return get_menu_item_by_id(menu_item_id)

@router.put("/{menu_item_id}")
def update(
    menu_item_id: str,
    menu_item: MenuItemUpdate
):
    return update_menu_item(
        menu_item_id,
        menu_item
    )
    

@router.delete("/{menu_item_id}")
def delete(menu_item_id: str):
    return delete_menu_item(menu_item_id)