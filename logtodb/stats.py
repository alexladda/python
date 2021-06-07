import sqlite3

DB_FILE = 'access_log.db'

conn = sqlite3.connect(DB_FILE)
r = conn.execute("""SELECT statuscode, COUNT()
                FROM access_log
                GROUP BY statuscode;""")
output = r.fetchall()

for statuscode in output:
    print("status code", statuscode[0], "-", statuscode[1], "times")
