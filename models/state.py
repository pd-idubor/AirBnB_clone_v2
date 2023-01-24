#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="delete",
                              backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """Return list of related city objects"""
            city_list = []
            cities_dict = storage.all(City)

            for val in cities_dict.values():
                if self.id == val.state_id:
                    city_list.append(val)
            return (city_list)
