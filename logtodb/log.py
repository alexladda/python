import time
import sys
import re
import sqlite3

# specify which log file to analyse with command line argument
LOGFILE = sys.argv[1]
# setting sqlite db file
DB_FILE = 'access_log.db'
# regex for nginx combined log format
LINEFORMAT = re.compile(
    r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""", re.IGNORECASE)


def watch(LOGFILE):
    # main loop to monitor the log file
    filepoll = open(LOGFILE, 'r')
    while True:
        newline = filepoll.readline()
        # first this will read all lines all lines and return them
        # after all existing lines are it will just return ''
        # then if a new line apperears, it will return that line

        if newline:
            currentline = re.search(LINEFORMAT, newline)
            if currentline:
                data = currentline.groupdict()
                print("log appended, writing to db:")
                print("============================")
                for item in data:
                    print(item, data[item], sep=": ")
                write(data)
                print(" ")
        else:
            time.sleep(0.5)


def write(data):
    # commiting data to the database
    conn = sqlite3.connect(DB_FILE)
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


def reset_database():
    # resetting database fresh every time the script is started
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""DROP TABLE IF EXISTS access_log""")
    conn.execute("""CREATE TABLE access_log (
                    ipaddress TEXT,
                    datetime TEXT,
                    url TEXT,
                    statuscode INTEGER,
                    bytessent INTEGER,
                    refferer TEXT,
                    useragent TEXT
                    )""")
    conn.commit()


reset_database()

watch(LOGFILE)
