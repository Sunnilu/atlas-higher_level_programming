#!/usr/bin/python3
'''
Script that lists all State objects that contain the letter a from the database
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Adjust import as per your module structure

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # MySQL connection parameters
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Ensure tables are created (not necessary if they already exist)
    Base.metadata.create_all(engine)

    # Query State objects containing the letter 'a', sorted by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    if states_with_a:
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
    else:
        print("")

    # Close the session
    session.close()
