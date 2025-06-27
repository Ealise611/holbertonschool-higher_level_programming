#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all rows from the
`states` table, ordered by the `id` column in ascending order.
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
        user="root",
        passwd="root",
        db="hbtn_0e_0_usa",
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
