#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models.place import place_amenity


class Amenity(BaseModel, Base):
    """class amenity that represents amenity for SQL db:
    Attributes:
        name: name
        place_amenities: place
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
