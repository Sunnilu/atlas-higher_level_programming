#!/usr/bin/python3
"""Script to link a class to a table in a MySQL database."""


import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy base class
Base = declarative_base()

class State(Base):
    """
    State class linked to the MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Establish database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the table in the database
    Base.metadata.create_all(engine)

