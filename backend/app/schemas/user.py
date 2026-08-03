from pydantic import BaseModel, EmailStr
from pydantic import BaseModel, EmailStr



class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str | None = None
    



class UserLogin(BaseModel):
    email: EmailStr
    password: str