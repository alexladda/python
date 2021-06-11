import sqlite3
import sys

try:
    DBFILE = sys.argv[1]
except IndexError:
    print("Please specify log file.")
    print("USAGE: $ python3 stats.py <path/to/logfile>")
    quit()


def read(DBFILE):
    conn = sqlite3.connect(DBFILE)
    r = conn.execute("""SELECT statuscode, COUNT()
                    FROM access_log
                    GROUP BY statuscode;""")
    output = r.fetchall()
    return output


if __name__ == "__main__":
    for statuscode in read(DBFILE):
        print("status code", statuscode[0], "-", statuscode[1], "times")
