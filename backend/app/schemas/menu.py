from pydantic import BaseModel


class MenuItemCreate(BaseModel):
    restaurant_id: str
    name: str
    description: str
    category: str
    price: float
    image_url: str | None = None
    is_available: bool = True



class MenuItemUpdate(BaseModel):
    restaurant_id: str
    name: str
    description: str
    category: str
    price: float
    image_url: str | None = None
    is_available: bool = True