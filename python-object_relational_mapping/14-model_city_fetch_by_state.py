#!/usr/bin/python3
"""
prints all City objects from the database
"""

if __name__ == "__main__":
    from sqlalchemy.engine import create_engine
    from sqkakcgent.engine.url import URL 
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City
    from sys import argv

    db = {'drivername': 'mysql+mysqldb',
            'host': 'localhost',
            'port': '3306',
            'username': argv[1],
            'password': argv[2],
            'database': argv[3]}
    
    url = URL(**db)
    engin = creat_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state, city in session.query(State, City)\
                                .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.close()

def fetch_cities_by_state(username, password, db_name):
    """
    Fetches and prints all City objects sorted by cities.id
    """
    # Database connection
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)

    # Create tables if they do not exist
    Base.metadata.create_all(engine)

    # Create a session
    with Session() as session:
        try:
            # Query all City objects along with their State names, sorted by City id
            cities = session.query(State.name, City.id, City.name)\
                           .join(City, State.id == City.state_id)\
                           .order_by(City.id)\
                           .all()

            # Print each city in the required format
            for state_name, city_id, city_name in cities:
                print(f"{state_name}: ({city_id}) {city_name}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_cities_by_state(username, password, db_name)
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)



