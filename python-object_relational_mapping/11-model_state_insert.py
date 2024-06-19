#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from model_state import Base, State  # Adjust this import according to your project structure

def add_state(username, password, db_name):
    """
    Adds a new State object to the database and prints its id.
    """
    engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost:3306/{db_name}")
    Session = sessionmaker(bind=engine)

    with Session() as session:
        try:
            existing_state = session.query(State).filter_by(name="Louisiana").first()
            if existing_state:
                print("State Louisiana already exists.")
            else:
                new_state = State(name="Louisiana")
                session.add(new_state)
                session.commit()
                print(f"New state added with id: {new_state.id}")
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    add_state(username, password, db_name)

