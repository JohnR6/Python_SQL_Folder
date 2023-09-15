import mysql.connector
import sqlite3

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print(conn)

cur = conn.cursor()

cur.execute("SHOW DATABASES")

for database in cur:
    print(database)