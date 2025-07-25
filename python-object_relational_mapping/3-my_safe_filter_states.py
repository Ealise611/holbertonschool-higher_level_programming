#!/usr/bin/python3
"""
This script takes in 4 arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
The script should take 4 arguments:
mysql username, mysql password, database name and state name searched
(safe from MySQL injection)
must use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
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
        charset="utf8"
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state_name:
            print(row)
    cur.close()
    conn.close()
