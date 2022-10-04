#!/usr/bin/python3
'''
    Implementation of the State class
'''
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base



class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            """
                Getter
            """
            city_dict = models.storage.all(models.classes["City"])
            city_list = []

            for key, value in city_dict.items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
