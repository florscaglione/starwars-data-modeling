import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    people_ = db.relationship('People', backref='user', lazy=True) #
    planets = db.relationship('Planet', backref='user', lazy=True) #
    starships = db.relationship('Starship', backref='user', lazy=True) #


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    height = Column(String(50))
    mass = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    name = Column(String(50), nullable=False)
    img_url: Column(String)
    homeworld = relationship("Planet", back_populates="people")
    user_id = Column(Integer, ForeignKey('user.id'))
   # user = relationship("User")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    diameter = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50))
    gravity = Column(String(50))
    population = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(String(50))
    name = Column(String(50), nullable=False)
    img_url: Column(String)
    people = relationship("People")
    user_id = Column(Integer, ForeignKey('user.id'))
   # user = relationship("User")

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    model = Column(String(50))
    starship_class = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(String(50))
    length = Column(String(50))
    crew = Column(String(50))
    passengers = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    hyperdrive_rating = Column(String(50))
    MGLT = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    name = Column(String(50), nullable=False)
    img_url: Column(String)
    #people = relationship("People", uselist=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    #user = relationship("User")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')