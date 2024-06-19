#!/usr/bin/python3
'''
Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Adjust this import according to your project structure

def delete_states_with_a(username, password, db_name):
    """
    Deletes all State objects with a name containing the letter 'a'.
    """
    # Database connection
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)

    # Create a session
    with Session() as session:
        try:
            # Query and delete State objects containing 'a' in their name
            states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
            if states_to_delete:
                for state in states_to_delete:
                    session.delete(state)
                session.commit()
                print(f"{len(states_to_delete)} state(s) deleted.")
            else:
                print("No states found with names containing 'a'.")
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    delete_states_with_a(username, password, db_name)
