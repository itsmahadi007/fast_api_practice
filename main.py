from fastapi import FastAPI
from app.sample_app.routes.books_view import router as books_router
from settings.middleware import setup_middleware

app = FastAPI()

setup_middleware(app)

app.include_router(books_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
