from fastapi import FastAPI

app = FastAPI(
    title="Urban Bite API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Urban Bite API!"
    }


