#!/usr/bin/python3
"""
Script that prints all City objects from the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    # Database connection parameters
    db = {
        'drivername': 'mysql+mysqldb',
        'host': 'localhost',
        'port': '3306',
        'username': argv[1],
        'password': argv[2],
        'database': argv[3]
    }
    
    # Constructing the URL for the database connection
    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    
    # Create all tables in the database if they do not exist
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    with Session(engine) as session:
        try:
            # Query all State and City objects and print them
            for state, city in session.query(State, City).filter(State.id == City.state_id).all():
                print(f"{state.name}: ({city.id}) {city.name}")
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()  # Rollback in case of error to avoid inconsistent state
