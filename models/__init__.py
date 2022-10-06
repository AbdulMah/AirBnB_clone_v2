#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
import os
from os import getenv

if (os.getenv("HBNB_TYPE_STORAGE") == "db"):
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
