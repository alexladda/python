# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:

def grow_string(word):
    output_string = word
    for i in range(1,len(word)):
        output_string = word[0:len(word)-i] + output_string
    return output_string


word = input("Word: ")
value = grow_string(word)
print(value)



































# Solution:

# def grow_string(str):
#   result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result
