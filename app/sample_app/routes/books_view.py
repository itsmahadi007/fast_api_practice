from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.sample_app.models.booksmodel import BooksModel
# from database import SessionLocal
# from crud.user import get_user, get_users, create_user
# from schemas.user import UserCreate, User

from app.sample_app.queries.base_queries import get_books_by_title, create_books
from app.sample_app.schema.schema import BooksSchema, BookBase
from settings.database import get_db

router = APIRouter()


@router.post("/books/", response_model=BooksSchema)
def create_books_route(book: BookBase, db: Session = Depends(get_db)):
    # check if book already exists
    db_books = get_books_by_title(db, title=book.title)
    if db_books:
        raise HTTPException(status_code=400, detail="Book already registered")
    return create_books(db=db, book=book)


@router.get("/books/{title}", response_model=BooksSchema)
def read_books(title: str, db: Session = Depends(get_db)):
    db_books = get_books_by_title(db, title=title)
    if db_books is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_books


@router.get("/books/", response_model=list[BooksSchema])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(BooksModel).offset(skip).limit(limit).all()
    return books

# @router.get("/users/", response_model=list[User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @router.get("/users/{user_id}", response_model=User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
