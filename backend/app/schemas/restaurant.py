from pydantic import BaseModel, EmailStr


class RestaurantCreate(BaseModel):
    name: str
    description: str
    cuisine: str
    address: str
    city: str
    phone: str
    email: EmailStr
    image_url: str | None = None
    opening_time: str
    closing_time: str
    delivery_fee: float
    minimum_order: float
    
    

class RestaurantUpdate(BaseModel):
    name: str
    description: str
    cuisine: str
    address: str
    city: str
    phone: str
    email: EmailStr
    image_url: str | None = None
    opening_time: str
    closing_time: str
    delivery_fee: float
    minimum_order: float