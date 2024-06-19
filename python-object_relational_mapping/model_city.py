#!/usr/bin/python3
"""Class definition of a city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base  # Import the Base class from model_state module

class City(Base):
    """City class that inherits from Base"""

    __tablename__ = 'cities'  # Table name in the database

    # Columns definition
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        """String representation of the City object"""
        return "<City(id={}, name='{}', state_id={})>".format(self.id, self.name, self.state_id)

if __name__ == "__main__":
    # Testing the City class
    # You can perform operations here to test the City class behavior
    pass

