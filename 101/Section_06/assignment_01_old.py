# Assignment 1:

import sys
import os
import re


# directory_containing_files = sys.argv[1]
# words_to_aggregate = sys.argv[2:]

dev_path = "/Users/alex/repo/python101/Section_06/project_files"
print(dev_path)
directory_containing_files = dev_path
words_to_aggregate = ["there", "Michael", "running"]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:


# Solution:
# words_and_counts = {}
#
# for word in words_to_aggregate:
#     count = 0
#     for path, folder_names, file_names in os.walk(directory_containing_files):
#         for file_name in file_names:
#             file = os.path.join(path, file_name)
#             with open(file, "r") as a_file:
#                 for line in a_file:
#                     if re.search(word, line):
#                         word_list = re.findall(word, line)
#                         count += len(word_list)
#
#     words_and_counts[word] = count
#
#
#
# print(words_and_counts)
