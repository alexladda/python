import time
import sys
import re
import sqlite3


def watch(logfile):
    filepoll = open(logfile, 'r')
    while True:
        newline = filepoll.readline()
        # first this will read all lines all lines and return them
        # after all existing lines are it will just return ''
        # then if a new line apperears, it will return that line

        if newline:
            currentline = re.search(lineformat, newline)
            data = currentline.groupdict()
            print("newline found")
            print("=============")
            print("writing to db: ", list(data.values()))
            write(data)
            print("             ")
        else:
            time.sleep(0.5)


def write(data):
    # try:
    conn = sqlite3.connect('access_log.db')

    conn.execute("""CREATE TABLE IF NOT EXISTS access_log (
                    ipaddress TEXT,
                    datetime TEXT,
                    url TEXT,
                    statuscode INTEGER,
                    bytessent INTEGER,
                    refferer TEXT,
                    useragent TEXT
                    )""")

    conn.execute("""INSERT INTO access_log VALUES (
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?)""",
                 list(data.values()))
    conn.commit()
    # except:
    #     print("Unable to connect to the database")
    #     quit()


logfile = sys.argv[1]
lineformat = re.compile(
    r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""", re.IGNORECASE)


watch(logfile)
