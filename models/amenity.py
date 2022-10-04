#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''

from os import environ
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""
