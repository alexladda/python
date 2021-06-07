# <open nginx (combined) log and read new lines>
# <parse lines>
# <store them in database>

import time
import sys


def watch(logfile):
    fp = open(logfile, 'r')
    while True:
        newline = fp.readline()
        # Once all lines are read this just returns ''
        # until the file changes and a new line appears

        if newline:
            data = re.search(lineformat, newline)
            print(data)
        else:
            time.sleep(0.5)


logfile = sys.argv[1]
lineformat = re.compile(
    r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""", re.IGNORECASE)


watch(logfile)
