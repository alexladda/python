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
            print(newline)
        else:
            time.sleep(0.5)


logfile = sys.argv[1]

watch(logfile)
