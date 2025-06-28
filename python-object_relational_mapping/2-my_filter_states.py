#!/usr/bin/python3
"""
This script takes in 4 arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
4 arguments are: mysql username, mysql password,
database name and state name searched
must use the module MySQLdb (import MySQLdb)
Must use format to create the SQL query with user input
Results must be sorted in ascending order by states.id
the code should not be executed when imported
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
        charset="utf8"
    )
    cur = conn.cursor()
    query = "SELECT * " \
    "FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state_name:
            print(row)
    cur.close()
    conn.close()
