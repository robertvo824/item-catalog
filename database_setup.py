import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    image = Column(String(250))
    create_date = Column(Date, nullable=False)
    last_update = Column(Date)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "name": self.name,
            "id": self.id,
        }


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    artist = Column(String(80), nullable=False)
    album = Column(String(250))
    description = Column(String(250))
    image = Column(String(250))
    year = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "artist": self.artist,
            "album": self.album,
            "description": self.description,
            "image": self.image,
            "year": self.year,
        }


engine = create_engine("sqlite:///catalog.db")
Base.metadata.create_all(engine)
