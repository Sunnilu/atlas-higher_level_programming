#!/usr/bin/python3
'''prints the State object with the name passed as argument from the database hbtn_0e_6_usa
'''

if __name__ == "__main__":
  from sqlalchemy import creat_engine
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy.orm import sessionmaker
  import sys
  from model_state import Base, State,

  inp = sys.argv
  if len(inp) < 5 or ";" in inp[4]:
    exit(1)

  conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
  engine = create_enging(conn_str.format(inp[1], inp[2], inp[3],))
  Session = sessionmaker(engine)

  Base.metadata.create_all(engine)

  session = Session()

  my_query = session.query(state).filter(State.name.like(inp[4])).all()

  if len(my_query) == 0:
    print("Not found")
  else:
    print(my_query[0].id
          
  session.close()
