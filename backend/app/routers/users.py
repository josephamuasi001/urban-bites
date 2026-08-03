from fastapi import APIRouter, Depends
from app.auth.auth_bearer import get_current_user

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

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):

    return {
        "message": "Authenticated user.",
        "user": current_user
    }