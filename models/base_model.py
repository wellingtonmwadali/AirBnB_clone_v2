#!/usr/bin/python3
"""The Base Model class"""
import models
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Datetime
from datetime import datetime

Base = declarative_base()
"""Creates a base class for declarative class definations"""


class BaseModel:
    """BaseModel class
    with attribute id"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def save(self):
        """Update time with current time"""
        self.updated_at = datetime.utcnow()
        models.storage.now(self)
        models.storage.save()

    def __init__(self, *args, **kwargs):
        """initialize the object with different combinations of
        arguments"""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def to_dict(self):
        """Dictionary representation of BaseModel"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Delete present instance from storage"""
        models.storage.delete(self)
        models.storage.save()

    def __str__(self):
        """String representation of BaseModel instance"""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
