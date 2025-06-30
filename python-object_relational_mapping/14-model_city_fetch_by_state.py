#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa:
Your script should take 3 arguments:
mysql username, mysql password and database name
must use the module SQLAlchemy
must import State and Base from model_state
- from model_state import Base, State
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
Results must be display as (<state name>: (<city id>) <city name>)
Your code should not be executed when imported
"""

from sqlalchemy import create_engine
# connect with the MySQL database
from sqlalchemy.orm import sessionmaker
# create a session to interact with the database
from model_state import Base, State
from model_city import City

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

    # Query all City objects and order by id
    cities = (
        session.query(State.name, City.id, City.name)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )
    # Print the results
    for state_name, city_id, city_name in cities:
        print(f"{state_name}: ({city_id}) {city_name}")
    # Close the session
    session.close()
