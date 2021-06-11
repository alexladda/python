# code challenge

# precursor

For the sake of brevity and clarity, these assumptions about the task were made:

- I limited myself to the use of standard python libraries. However sqlalchemy and pandas would offer themselves for further development.
- The scripts will be run on the same (Unix) machine as the log files.
- Log rotation was not considered.

# usage

`$ python3 log.py <path/to/logfile> <path/to/dbfile>`

This will start the service that will continually monitor the specified log file. It will read all existing lines, write them to a sqlite database file, and will run until interrupted (CTRL - C).

`$ python3 stats.py <path/to/dbfile>`

This runs the required SQL query against the specified file and prints the output to the console.


# unittest

These scripts were developed as a proof of concept and not with Test Driven Development methodology. Only very basic exception handling and unit testing was implemented to show familiarity with the concept.

`$ python3 -m log_test.py
