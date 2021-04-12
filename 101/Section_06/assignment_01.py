# Assignment 1:

import sys
import os
import re

# Example input:
# > python module.py folder there Michael running

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:

# getting command line arguments
directory_containing_files = sys.argv[1]
words_to_aggregate = sys.argv[2:]

# initializing words_and_counts dictionary
words_and_counts = {}
for word in words_to_aggregate:
    words_and_counts[word] = 0

# walking through the whole directory tree
for dirpath, dirnames, filenames in os.walk(directory_containing_files):
    # unpacking the list of files for each directory
    for file in filenames:
        # opening each file
        with open(os.path.join(dirpath, file), mode="r") as current_file:
            # loading file into string variable
            contents = current_file.read()
            # checking the search terms against the sting
            for word in words_to_aggregate:
                # creating match object (list of strings)
                match = re.findall(word, contents)
                # adding up into dictionary
                words_and_counts[word] += len(match)

print("final count: ", words_and_counts)
