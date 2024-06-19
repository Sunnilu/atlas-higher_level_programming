#!/usr/bin/python3
"""
Script that lists State objects based on conditions.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Assuming this is correctly defined elsewhere

def main(username, password, dbname):
    engine = create_engine(f'mysql+pymysql://{username}:{password}@localhost:3306/{dbname}')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        query_result = session.query(State).filter(State.name.contains('a')).order_by(State.id.asc()).all()
        if not query_result:
            print("No record")
        else:
            for index, state in enumerate(query_result, start=1):
                print(f"{index}: {state.name}")
    finally:
        session.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv)!= 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
