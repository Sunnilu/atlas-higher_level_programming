#!/usr/bin/python3
"""
Script that lists State objects based on conditions.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Adjust this import according to your project structure

def connect_to_db(username, password, db_name):
    """
    Connects to the MySQL database and returns a session object.
    """
    engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost:3306/{db_name}")
    Session = sessionmaker(bind=engine)
    return Session()

def get_states_with_a(session):
    """
    Queries the database for states containing the letter 'a' and returns them sorted by id.
    """
    result = session.query(State).filter(State.name.contains('a')).order_by(State.id.asc()).all()
    return result

def display_results(states):
    """
    Displays the states in the desired format.
    """
    if not states:
        print("No record")
    else:
        for index, state in enumerate(states, start=1):
            print(f"{index}: {state.name}")

def main():
    """
    Main function to handle command line arguments and interact with the database.
    """
    if len(sys.argv)!= 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    session = connect_to_db(username, password, db_name)
    try:
        states = get_states_with_a(session)
        display_results(states)
    finally:
        session.close()

if __name__ == "__main__":
    main()

