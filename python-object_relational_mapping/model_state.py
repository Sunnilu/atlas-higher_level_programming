#!/usr/bin/python3
"""Script to link a class to a table in a MySQL database."""

from sys import argv  # Import argv to retrieve command-line arguments
from model_state import Base, State  # Import SQLAlchemy Base and State class
from sqlalchemy import create_engine  # Import create_engine from SQLAlchemy

if __name__ == "__main__":
    # Construct the database connection string using command-line arguments
    # argv[1]: MySQL username
    # argv[2]: MySQL password
    # argv[3]: Database name
    db_connection_str = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])

    # Create the SQLAlchemy engine
    engine = create_engine(db_connection_str, pool_pre_ping=True)

    # Create the tables defined in the Base's metadata in the database
    Base.metadata.create_all(engine)

