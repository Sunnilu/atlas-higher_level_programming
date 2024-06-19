#!/usr/bin/python3
"""Python file that contains that class definition of a State and an instance
"""

from sqlalchemy import Column, Integer, String  # Corrected import for String type
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base

    Attributes:
        id: Id state
        name: Name of state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)  # Corrected type from string to String
