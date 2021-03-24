# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

# Your Code Below:

# my_list= list(range(1,11))
# print(my_list)
#
# def check123(list):
#     needle_in_haystack = [1,2,3]
#     cases_to_test = len(list) - len(needle_in_haystack) + 1
#     if cases_to_test > 0:
#         for i in range(0,cases_to_test):
#             window=list[i:(i+3)]
#             print(window)
#             if window == needle_in_haystack:
#                 return True
#
# print(check123(my_list))

def checkany(list, needle_in_haystack = [1,2,3]):
    cases_to_test = len(list) - len(needle_in_haystack) + 1
    if cases_to_test > 0:
        for i in range(0,cases_to_test):
            window=list[i:(i+2)]
            if window == needle_in_haystack:
                return True
    return False

from random import shuffle

my_list = list(range(0,10))
to_find = list(range(0,2))

for i in range (0,100):
    shuffle(my_list)
    shuffle(to_find)
    print(my_list, to_find, checkany(my_list,to_find))

# def checkshort(list):
#     for i in range(0,len(list)-2):
#         if list[i] == 1 and list[i+1] == 2 and list[i+2] == 3:
#             return True
#     return False

# print(checkshort([1, 2, 3, "a"]))




































# Solution:

# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
