#!/usr/bin/python3
"""
This script changes the the name of
a State object from the database hbtn_0e_6_usa
Script should take 3 arguments: mysql username, mysql passwd and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
change the name of the State where id = 2 to New Mexico
code should not be executed when imported
"""

from sqlalchemy import create_engine
# connect with the MySQL database
from sqlalchemy.orm import sessionmaker
# create a session to interact with the database
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine that connects to the MYSQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # change the name of the State where id = 2 to New Mexico
    new_state = session.query(State).filter(State.id == 2).first()
    if new_state is None:
        print("Not found")
    else:
        new_state.name = "New Mexico"
        session.commit()
    # Close the session
    session.close()
