from sqlalchemy.orm import Session
import logging

from app.sample_app.models.booksmodel import BooksModel
from app.sample_app.schema.schema import BookBase

logger = logging.getLogger(__name__)

def get_books_by_title(db: Session, title: str):

    try:
        return db.query(BooksModel).filter(BooksModel.title == title).first()
    except Exception as e:
        logger.warning(f"Error: {e} -------------")
        return None


def create_books(db: Session, book: BookBase) -> BooksModel:
    db_book = BooksModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

