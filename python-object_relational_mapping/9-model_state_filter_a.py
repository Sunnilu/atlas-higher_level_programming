#!/usr/bin/env python3
"""
Script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py mysql_username mysql_password database_name")
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create connection string
    connection_string = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"

    # Create engine and session
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for states containing letter 'a' and sort by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
