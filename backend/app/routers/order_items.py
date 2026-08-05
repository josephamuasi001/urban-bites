from fastapi import APIRouter

from app.schemas.order_item import (
    OrderItemCreate,
    OrderItemUpdate
)

from app.services.order_item_service import (
    create_order_item,
    get_all_order_items,
    get_order_item_by_id,
    update_order_item,
    delete_order_item
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


@router.put("/{order_item_id}")
def update_item(
    order_item_id: str,
    order_item: OrderItemUpdate
):

    return update_order_item(
        order_item_id,
        order_item
    )
    
    

@router.delete("/{order_item_id}")
def delete_item(order_item_id: str):

    return delete_order_item(
        order_item_id
    )
    

