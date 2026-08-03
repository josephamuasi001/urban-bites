from fastapi import APIRouter

from app.schemas.user import UserCreate, UserLogin
from app.services.user_service import create_user
from app.services.user_service import (
    create_user,
    get_all_users,
    login_user
)
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def get_users():
    return get_all_users()


@router.post("/register")
def register(user: UserCreate):

    return create_user(user)


@router.post("/login")
def login(user: UserLogin):

    return login_user(user)