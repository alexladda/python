# shuffle a list with numbers from 1 to 100

from random import shuffle

my_list = []
x=0

while x <= 100:
    my_list.append(x)
    x += 1

shuffle(my_list)
print(my_list)


# or ...

my_list = list(range(1,101))
shuffle(my_list)
print(my_list)
