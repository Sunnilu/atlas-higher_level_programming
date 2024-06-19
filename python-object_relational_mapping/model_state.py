#!/usr/bin/python3
"""Script to link a class to a table in a MySQL database."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class City(Base):
    """Class representing the 'cities' table in the database."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))  # Foreign key referencing states.id
    state = relationship("State", back_populates="cities")  # Relationship with State class

class State(Base):
    """Class representing the 'states' table in the database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")  # Relationship with City class

