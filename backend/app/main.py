from fastapi import FastAPI
from app.database.supabase import supabase

app = FastAPI(
    title="Urban Bite API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Urban Bite API!"
    }


@app.get("/test-db")
def test_db():

    response = supabase.table("test").select("*").execute()

    return response.data