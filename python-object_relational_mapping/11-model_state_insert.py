#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Adjust this import according to your project structure

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Database connection
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create tables if they do not exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Check if the state already exists
        existing_state = session.query(State).filter_by(name='Louisiana').first()
        if existing_state:
            print("State Louisiana already exists.")
        else:
            # Add new state
            new_state = State(name='Louisiana')
            session.add(new_state)
            session.commit()
            print(f"New state added with id: {new_state.id}")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()
