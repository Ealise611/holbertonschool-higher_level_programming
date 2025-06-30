#!/usr/bin/python3
"""
This script prints the State objects with the 'name' passed as an argument 
from the database hbtn_0e_6_usa
script should take 4 arguments:
mysql username, mysql password, database name, state name to search
must import State and Base from model_state
- from model_state import Base, State
must use the module SQLAlchemy (import sqlalchemy)
script should connect to a MySQL server running on localhost at port 3306
Result must display the states.id
If no states match the search, print "Not found" followed by a new line
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
    state_name = sys.argv[4]

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
    # Query all State objects and print the state.id if it matches the state_name
    states = (
        session.query(State)
        .filter(State.name == state_name)
        .order_by(State.id)
        .all()
    )
    # Print the results
    if states:
        for state in states:
            print(f"{state.id}")
    else:
        print("Not found")
    # Close the session
    session.close()
    