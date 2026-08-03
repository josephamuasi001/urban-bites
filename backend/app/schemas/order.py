from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    menu_item_id: str
    quantity: int


class OrderCreate(BaseModel):
    restaurant_id: str
    items: list[OrderItemCreate]