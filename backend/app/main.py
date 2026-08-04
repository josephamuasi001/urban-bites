from fastapi import FastAPI

from app.database.supabase import supabase

from app.routers.orders import router as order_router

from app.routers.menus import router as menu_router

from app.routers.reviews import router as review_router

from app.routers.users import router as user_router
from app.routers.restaurants import router as restaurant_router

app = FastAPI(
    title="Urban Bite API",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(restaurant_router)
app.include_router(menu_router)
app.include_router(order_router)
app.include_router(review_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Urban Bite API!"
    }


@app.get("/test-db")
def test_db():

    response = supabase.table("test").select("*").execute()

    return response.data