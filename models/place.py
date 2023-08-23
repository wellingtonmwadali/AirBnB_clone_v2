#!/usr/bin/python3
"""script that inherits from BaseModel"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import environ as env


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey("places.id")),
    Column('amenity_id', String(60), ForeignKey("amenities.id"))
)


class Place(BaseModel, Base):
    """class for Place
    Attributes of class Place:
        city_id: city id
        user_id: user id
        name: name input
        description: description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: price per night
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    __reviews = relationship("Review", cascade="all, delete", backref="place")
    __amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        backref="place",
        viewonly=False
    )

    @property
    def reviews(self):
        """function that gets all reviews from file storage
        with the current place id
        """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__reviews
        list = [
            x for y, x in models.storage.all(models.Review).items()
            if x.place_id == self.id
        ]
        return (list)

    @property
    def amenities(self):
        """function that get all amenities with the current place id
        """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__amenities
        list = [
            x for y, x in models.storage.all(models.Amenity).items()
            if x.id in self.amenity_ids
        ]
        return (list)
