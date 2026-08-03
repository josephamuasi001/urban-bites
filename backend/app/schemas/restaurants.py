from pydantic import BaseModel, EmailStr


class RestaurantCreate(BaseModel):
    name: str
    description: str
    address: str
    phone: str
    email: EmailStr
    image_url: str
    opening_time: str
    closing_time: str
    is_open: bool = True