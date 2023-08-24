#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import os
import json
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format
    serialization and decerialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as q:
            w = {x: y.to_dict() for x, y in FileStorage.__objects.items()}
            json.dump(w, q)

    def classes(self):
        """define class that returns a dictionary of valid classes
        and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
                  }
        return classes

    def reload(self):
        """Loads storage dictionary from file"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as q:
            obj_dict = json.load(q)
            obj_dict = {x: self.classes()[y["__class__"]](**y)
                        for x, y in obj_dict.items()}
            FIleStorage.__objects = obj_dict

    def delete(self, obj=None):
        """define delete that deletes obj from __objects"""
        if obj is not None:
            del self.__objects[obj.__class__.__name__ + '.' + obj.id]
            self.save()

    def close(self):
        """call reload() for decserialization"""
        self.reload()
