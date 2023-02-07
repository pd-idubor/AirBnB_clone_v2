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
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City",
                              cascade="all, delete, delete-orphan",
                              backref="state")

    else:
        @property
        def cities(self):
            """Return list of related city objects"""
            from models import storage
            city_list = []
            cities_dict = storage.all(City)

            for val in cities_dict.values():
                if self.id == val.state_id:
                    city_list.append(val)
            return (city_list)
