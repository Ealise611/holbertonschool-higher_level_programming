#!/usr/bin/python3
"""
This script  takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
 script should take 4 arguments:
 mysql username, mysql password, database name and state name
 (SQL injection free!)
must use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
use only execute() once
code should not be executed when imported
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cur = conn.cursor()
    # Use a JOIN to get cities associated with the state name
    # and filter by the state name provided as an argument.
    # The query retrieves city names from the cities table
    # where the state name matches the provided state name.
    # The results are ordered by cities.id in ascending order.
    # If no cities are found, it prints "No result".
    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    cities = ", ".join([row[0] for row in query_rows])
    print(cities)
    cur.close()
    conn.close()
