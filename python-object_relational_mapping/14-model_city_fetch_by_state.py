#!/usr/bin/python3
'''Script that prints all City objects from the database hbtn_0e_14_usa, including their associated State names.'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities_by_state(username, password, db_name):
    """
    Fetches and prints all City objects sorted by cities.id, including their associated State names.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Name of the database to connect to.

    Prints:
        Each city's state name followed by its ID and name, sorted by city ID.
    """
    # Database connection
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)

    # Create tables if they do not exist
    Base.metadata.create_all(engine)

    # Create a session
    with Session() as session:
        try:
            # Query all City objects sorted by id
            cities = session.query(City).order_by(City.id).all()

            if cities:
                for city in cities:
                    print(f"{city.state.name}: ({city.id}) {city.name}")
            else:
                print("No cities found.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv)!= 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_cities_by_state(username, password, db_name)
