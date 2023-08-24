#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel
from models.base_model import Base
from models.state import State
from sqlalchemy import Column, String, foreignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Atrributes:
        state_id: state id
        name: name
        places: place
    """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("State.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="delete", backref="cities")
