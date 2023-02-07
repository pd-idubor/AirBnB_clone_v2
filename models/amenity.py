#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, ForeignKey, Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.place import Place, place_amenity


class Amenity(BaseModel, Base):
    """Amenities class"""
    __tablename__ = "amenities"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity,
                                       back_populates='amenities')

    else:
        name = ""
