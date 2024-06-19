#!/usr/bin/python3
"""Script to link a class to a table in a MySQL database."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Define City class representing another table in the database
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))  # Foreign key referencing states.id
    state = relationship("State", back_populates="cities")  # Relationship with State class

# Define State class with a relationship to City
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")  # Relationship with City class

