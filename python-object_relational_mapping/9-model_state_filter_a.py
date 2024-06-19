#!/usr/bin/python3
'''
Script that list all state objects that contain the letter a from the database
using module SQLAlchemy
'''

import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Adjust this import according to your project structure

def connect_to_db(username, password, db_name):
    """
    Establishes a connection to the MySQL database.
    """
    engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost:3306/{db_name}")
    Session = sessionmaker(bind=engine)
    return Session()

def query_and_display_states(session):
    """
    Queries the database for states containing the letter 'a', sorts them, and displays them.
    """
    query = text("SELECT * FROM states WHERE name LIKE :search_term ORDER BY id ASC;")
    states = session.execute(query, {'search_term': '%a%'}).fetchall()
    if not states:
        print("No record")
    else:
        for index, state in enumerate(states, start=1):
            print(f"{index}: {state['name']}")

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
        query_and_display_states(session)
    finally:
        session.close()

if __name__ == "__main__":
    main()

