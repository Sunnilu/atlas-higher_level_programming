#!/usr/bin/python3
'''
changes the name of a State object from the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Adjust this import according to your project structure

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Database connection
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session
    with Session() as session:
        try:
            # Query the State object by id (assuming id=2 as per your example)
            state_to_update = session.query(State).filter_by(id=2).first()

            if state_to_update:
                # Change the name attribute
                state_to_update.name = 'New Mexico'

                # Commit the change to the database
                session.commit()
                print("State name updated successfully.")
            else:
                print("State with id=2 not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()






