list_a = ['a','b','c','d','e','f']
list_b = [1,2,3,4,5,6]
list_c = [99,98,97,96,95,94]

print(zip(list_a, list_b, list_c))
print(list(zip(list_a, list_b, list_c)))

zipped_list = list(zip(list_a, list_b, list_c))

for a,b,c in zipped_list:
    print(a, b, c)


print('z' in list_a)
print('a' in list_a)

print('john' in {'john':140})
print(140 in {'john':140})  # by default only keys -> evaluates to False
print(140 in {'john':140}.values())              # -> evaluates to True


print(max(list_b))
print(min(list_c))

print(max(list_a))
print(min(list_a))

from random import randint
random_number = randint(0,1000)
print(random_number)

from random import shuffle
my_list = list_b
shuffle(my_list)
print(my_list)
