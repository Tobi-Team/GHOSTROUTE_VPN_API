from sqlalchemy import (
    Boolean, Column, Integer,
    String, Text, Float, ForeignKey
)
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(121), unique=True, index=True)  # unique email
    username = Column(String(101), unique=True, index=True)  # unique username
    password = Column(String(200))

    # slug = Column(String(200))
    is_activated = Column(Boolean)
