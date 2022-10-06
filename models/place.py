#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import os
from os import getenv
from models.base_model import Base, BaseModel
from models.review import Review
from models.amenity import Amenity
import sqlalchemy
from sqlalchemy import Table, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column(
                             'place_id', String(60), ForeignKey('places.id'),
                             nullable=False, primary_key=True
                      ),
                      Column(
                             'amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False, primary_key=True
                      ))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        __tablename__ : represents the table name
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = "places"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
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
        reviews = relationship("Review", passive_deletes=True, backref="place")
        amenities = relationship(
                                 "Amenity", secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Returns the list of Review instances
            """
            review_dict = models.storage.all('Review')
            review_list = []
            for rev in review_dict.values():
                if rev.place_id == self.id:
                    review_list.append(rev)
            return rev

        @property
        def amenities(self):
            """
            Getter
            Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            obj_list = []
            objs = models.storage.all('Amenity')
            for amen in objs.value():
                if amen.id in amenities_ids:
                    obj_list.append(amen)
            return obj_list

        @amenities.setter
        def amenities(self, obj):
            """
            Setter
            Handles append method for adding an Amenity.id
            to the attribute amenity_ids
            """
            if isinstance(obj, Amenity):
                if self.id == obj.place_id:
                    self.amenity_ids.append(obj.id)
