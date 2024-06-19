#!/usr/bin/python3
'''Script to manage database operations for cities and states.'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    db = {
        'drivername': 'mysql+mysqldb',
        'host': 'localhost',
        'port': '3306',
        'username': argv[1],
        'password': argv[2],
        'database': argv[3]
    }

    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for state, city in session.query(State, City).filter(State.id == City.state_id).all():
            print(f"{state.name}: ({city.id}) {city.name}")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()
