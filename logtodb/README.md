# code challenge

# precursor

For the sake of brevity and clarity, these assumptions about the task were made:

- I limited myself to the use of standard python libraries. However sqlalchemy and pandas would offer themselves for further development.
- The scripts will be run on the same (Unix) machine as the log files.
- These scripts were developed as a proof of concept and not with Test Driven Development methodology. Only very basic exception handling was implemented to show familiarity with the concept.
- You will find a very basic unit test to show my familiarity with the concept.

# usage

`$ python3 log.py <path/to/logfile>

(if no path is specified, it will default to /var/log/nginx/access.log)


## what does log.py do?

usage:

<open nginx (combined) log and read new lines>
<parse lines>
<store them in database>



## what does stats.py do?

<query db for records, group by status code>
<print>
