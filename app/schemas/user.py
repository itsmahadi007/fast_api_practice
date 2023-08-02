from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class UserBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: str

    class Config:
        orm_mode = True
