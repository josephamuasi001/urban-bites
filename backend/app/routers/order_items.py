from fastapi import APIRouter

from app.schemas.order_item import OrderItemCreate
from app.services.order_item_service import (
    create_order_item,
    get_all_order_items,
    get_order_item_by_id
)

router = APIRouter(
    prefix="/order-items",
    tags=["Order Items"]
)


@router.post("/")
def add_order_item(order_item: OrderItemCreate):

    return create_order_item(order_item)


@router.get("/")
def get_order_items():

    return get_all_order_items()


@router.get("/{order_item_id}")
def get_order_item(order_item_id: str):

    return get_order_item_by_id(order_item_id)