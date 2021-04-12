import sys
import re


# print(sys.argv)
#
# for argument in sys.argv:
#     print(argument)
#
# print(re.findall("is", "This is Miss Fiss"))
# print(re.findall(sys.argv[1], sys.argv[2]))

# defining a match object x
x = re.findall("is", "This is Miss Fiss")

if x:
    print("findall:      ", x)

y = re.search("ai", "The Rain in Spain")
# Returns a Match object, None if nothing found
print(y)
# original String to be searched
print("search string: ", y.string)
# returns a tuple with the position within original String
print("search span:   ", y.span())
# will show the whole word (if exactly one match)
print("search group:  ", y.group())
