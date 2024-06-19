#!/usr/bin/python3
'''Prints the State object with the name passed as argument from the database hbtn_0e_6_usa'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

# Check for correct number of arguments and avoid SQL injection
inp = sys.argv
if len(inp) < 5 or ";" in inp[4]:
    print("Usage: script.py <mysql_username> <mysql_password> <database_name> <state_name>")
    exit(1)

conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
Session = sessionmaker(bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(engine)

session = Session()

# Escape the input to prevent SQL injection
escaped_name = f"%{inp[4]}%"
my_query = session.query(State).filter(State.name.like(escaped_name)).order_by(State.id).first()

if my_query is None:
    print("Not found")
else:
    print(my_query.id)

session.close()
