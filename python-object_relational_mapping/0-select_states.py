#!/usr/bin/env python3
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="sqluser",
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
# This script connects to a MySQL database and retrieves all state IDs from the 'states' table,
# ordering them in ascending order. It prints each ID on a new line.
