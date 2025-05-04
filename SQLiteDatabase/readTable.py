import sqlite3

connection= sqlite3.connect('BelgiumCampus.db')

cursor=connection.execute("SELECT*from Lecturer")

for row in cursor:
    print(row)