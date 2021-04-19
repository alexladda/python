import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')

conn.execute("""CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                author TEXT,
                pages INTEGER,
                published INTEGER
                )""")

values = ('Deep Learning',
          'Ian Goodfellow et al.',
          775,
          datetime(2016, 11, 18).timestamp())

conn.execute("""INSERT INTO books VALUES (?, ?, ?, ?)""", values)

r = conn.execute("""SELECT * FROM books""")
output = r.fetchall()

print(output)
