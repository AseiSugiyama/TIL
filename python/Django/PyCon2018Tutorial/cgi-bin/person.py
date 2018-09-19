#!/usr/bin/env python
import sqlite3

DATABASE_NAME = 'cgi-bin/person.sqlite'

with sqlite3.connect(DATABASE_NAME) as connection:
    cursor = connection.cursor()
    cursor.execute("select * from person;")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
