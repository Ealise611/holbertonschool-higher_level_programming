#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
script should take 3 arguments: mysql username, mysql password and database name
must use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
code should not be executed when imported
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
