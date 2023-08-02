from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, ARRAY
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String, nullable=True)
    gender = Column(String)  # Here, change Enum to String
    roles = Column(ARRAY(String))  # Here, change Enum to String
