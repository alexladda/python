

my_list = ['computer', 'car', 'bottle', 'tv']


for item in my_list:
    # let's do this next week
    pass

# do other stuff
type(str)


for item in (1,2,3,4):
    # tuple
    print(item)

for item in [1,2,3,4]:
    # list
    print(item)

for item in "hello world":
    # string
    print(item)

# for item in 1234:
#     # 'int' object is not iterable
#     print(item)

my_dict = {"name": "elsa", "job":"ice princess"}

for item in my_dict:
    print(item + ":", end=" ")
    print(my_dict[item])
