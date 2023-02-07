#!/usr/bin/python3
"""Describes DBStorage class"""
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """Database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""

        connect = "mysql+mysqldb://{}:{}@{}/{}"
        db = getenv('HBNB_MYSQL_DB', default=None)
        username = getenv('HBNB_MYSQL_USER', default=None)
        passwd = getenv('HBNB_MYSQL_PWD', default=None)
        host = getenv('HBNB_MYSQL_HOST', default=None)

        self.__engine = create_engine(
                connect.format(username, passwd, host, db), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query of current database session"""

        result = []
        objects_dict = {}
        if cls is not None:
            result = self.__session.query(cls).all()
            for obj in result:
                key = obj.__class__.__name__ + '.' + obj.id
                objects_dict[key] = (obj)
        else:
            classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            for name in classes:
                try:
                    result = self.__session.query(eval(name)).all()
                    for obj in result:
                        key = obj.__class__.__name__ + '.' + obj.id
                        objects_dict[key] = (obj)
                except Exception:
                    pass

        return (objects_dict)

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)

        self.__session = Session()

    def close(self):
        """Closes a session"""
        self.__session.close()
