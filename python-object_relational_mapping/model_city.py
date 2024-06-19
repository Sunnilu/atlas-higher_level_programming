#!/usr/bin/python3
'''Model to define the City class and its relationship with the State class.'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """City class to map to the cities table in the database.

    Attributes:
        id (int): Unique identifier for each city.
        name (str): Name of the city.
        state_id (int): Foreign key referencing the state's ID.
        state (State): Relationship to the State class, representing the state the city belongs to.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Establishing relationship to State
    state = relationship("State", back_populates="cities")


