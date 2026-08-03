from fastapi import FastAPI

from app.routers.restaurants import router as restaurant_router
from app.database.supabase import supabase
from app.routers.users import router as user_router


app = FastAPI(
    title="Urban Bite API",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(restaurant_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Urban Bite API!"
    }


@app.get("/test-db")
def test_db():

    response = supabase.table("test").select("*").execute()

    return response.data