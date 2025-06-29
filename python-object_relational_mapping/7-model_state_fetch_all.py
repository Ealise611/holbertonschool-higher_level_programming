#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_6_usa
script should take 3 arguments:
mysql username, mysql password and database name
must use the module SQLAlchemy (import sqlalchemy)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The code should not be executed when imported
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
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()
    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
    # Close the session
    session.close()
    # Close the engine connection
    engine.dispose()

