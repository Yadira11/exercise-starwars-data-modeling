import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

'''Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')'''

Base = declarative_base()

class Favoritos(Base):
    __tablename__ = 'Favoritos'
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    personas_id = Column(Integer, ForeignKey('personas.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    genero = Column(String(250))
    correo = Column(String(250))
    telefono = Column(String(250))
    password = Column(String(250))


    
class planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(Integer)
    gravity = Column(String(250))
    climate = Column(String(250))
    orbital_period = Column(Integer)
    population = Column(Integer)

class Personas(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    birth_year = Column(String(250))
    skin_color = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    def to_dict(self):
        return {}
render_er(Base, 'diagram.png')