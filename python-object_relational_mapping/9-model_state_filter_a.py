#!/usr/bin/python3
"""
This script prints all State objects contains 'a'
from the database hbtn_0e_6_usa
script should take 3 arguments:
mysql username, mysql password and database name
must import State and Base from model_state
- from model_state import Base, State
must use the module SQLAlchemy (import sqlalchemy)
script should connect to a MySQL server running on localhost at port 3306
The state displayed must be the first in states.id
If the table states is empty, print "Nothing" follow by a new line
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

    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query all State objects and order by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
    # Close the session
    session.close()
