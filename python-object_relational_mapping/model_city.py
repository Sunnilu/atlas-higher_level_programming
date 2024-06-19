#!/usr/bin/python3
''' model to fetch city by state
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_base import Base

class State(Base):
    """State class to map to the states table in the database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Relationship to City
    cities = relationship("City", order_by=City.id, back_populates="state")
