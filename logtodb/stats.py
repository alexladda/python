import sqlite3

conn = sqlite3.connect('access_log.db')

r = conn.execute("""SELECT statuscode, COUNT()
                FROM access_log
                GROUP BY statuscode;""")

output = r.fetchall()

for statuscode in output:
    print("status code", statuscode[0], "-", statuscode[1], "times")
