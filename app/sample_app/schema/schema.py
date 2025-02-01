from pydantic import BaseModel, EmailStr


class BookBase(BaseModel):
    title: str
    author: str
    year: int


class BooksSchema(BookBase):
    id: int

    class Config:
        from_attributes = True
