#!/usr/bin/python3
""" class User"""
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
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
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        passwd = Column('password', String(128), nullable=False)
        f_name = Column(String(128), nullable=True)
        l_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="delete-orphan")
        reviews = relationship("Review", backref="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """initializes user class"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """modifying the password values """
        self._password = pwd
