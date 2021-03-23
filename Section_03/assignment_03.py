# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
# Your Code Below:

my_list = [1,2,3,'some data']
my_string = 'there will be multiple words and letters'


def multi_merge(list_arg, string_arg):
    words = string_arg.split()
    characters = list(string_arg)
    return list_arg + words + characters

merged_list = multi_merge(my_list, my_string)
print(merged_list)









































# Solution:

# def multi_merge(list_a, str):
#     return list_a + str.split() + list(str)
#
# print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))
