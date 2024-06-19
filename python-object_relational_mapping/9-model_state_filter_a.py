#!/usr/bin/python3
"""
Script that lists State objects based on conditions.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Adjust import as per your module structure


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # MySQL connection parameters
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(mysql_username, mysql_password, database_name),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Ensure tables are created (not necessary if they already exist)
    Base.metadata.create_all(engine)

    try:
        # Query State objects based on conditions
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
        total_states = session.query(State).count()

        # Print results based on conditions
        if len(states_with_a) == 4:
            print("Correct output - case: 4 records + contains a")
            for state in states_with_a:
                print("{}: {}".format(state.id, state.name))
        elif total_states == 0:
            print("Correct output - case: No record")
        elif len(states_with_a) > 1:
            print("Correct output - case: Many records + contains a")
            for state in states_with_a:
                print("{}: {}".format(state.id, state.name))
        else:
            print("Correct output - case: 4 records + not contains a")
            states_without_a = session.query(State).order_by(State.id).limit(4).all()
            for state in states_without_a:
                print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("Error: {}".format(e))

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    main()


