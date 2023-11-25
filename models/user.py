#!/usr/bin/python3
""" class User"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String


class User(BaseModel, Base):
    """class that represents user
    Atrributes:
        __tablename__: name for sql table
        email: user email address.
        passwd: user's password.
        f_name: user's first name
        l_name: user's last name
        places: user-pace relationship
        reviews: user-review"""
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
