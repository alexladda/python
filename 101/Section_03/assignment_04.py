# Assignment 4:

"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.

Example:

    For example, the below function call should return ['mike', 'john']

    last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])

"""

# Your code below:

this_list=[1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john']

def last_list(*args):
    pop_list = list(args)
    return pop_list.pop()

print(last_list(this_list))

print(last_list([1,2,3], [9,9,9], ['a','b','c']))





























# Solution:

# def last_list(*args):
#     return args[-1 :len(args)]
