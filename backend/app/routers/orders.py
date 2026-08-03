from fastapi import APIRouter, Depends

from app.auth.auth_bearer import get_current_user
from app.services.order_service import (
    create_order,
    get_all_orders,
    get_my_orders,
    update_order_status
)


from app.schemas.order import (
    OrderCreate,
    OrderStatusUpdate
)

from app.services.order_service import (
    create_order,
    get_all_orders
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
def place_order(
    order: OrderCreate,
    current_user=Depends(get_current_user)
):

    return create_order(
        order,
        current_user["sub"]
    )


@router.get("/")
def orders():
    return get_all_orders()


@router.get("/my-orders")
def my_orders(current_user=Depends(get_current_user)):

    return get_my_orders(
        current_user["sub"]
    )

@router.put("/{order_id}/status")
def change_order_status(
    order_id: str,
    order: OrderStatusUpdate
):

    return update_order_status(
        order_id,
        order.status
    )