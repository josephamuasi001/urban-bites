from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    order_id: str
    menu_item_id: str
    quantity: int
    price: float
    

class OrderItemUpdate(BaseModel):
    order_id: str
    menu_item_id: str
    quantity: int
    price: float