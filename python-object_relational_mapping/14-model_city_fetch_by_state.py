#!/usr/bin/python3
'''Script to manage database operations for cities and states.'''
import sys
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def create_tables_and_add_records(username, password, db_name):
    """
    Creates tables for States and Cities, adds initial records, and displays them.
    
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Name of the database to connect to.
        
    Prints:
        Initial records added to the database.
    """
    engine = create_engine(f'mysql+pymysql://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Ensure tables are created
        Base.metadata.create_all(engine)
        
        # Add initial records
        initial_states = ["California", "Texas", "Florida", "New York"]
        for state_name in initial_states:
            state = State(name=state_name)
            session.add(state)
        
        session.commit()
        print("Initial states added successfully.")
        
        # Display records
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"ID: {state.id}, Name: {state.name}")
            
    except exc.SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    if len(sys.argv)!= 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    create_tables_and_add_records(username, password, db_name)

