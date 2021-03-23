my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', ['orange', 'lime', 'lemon'], 'banana'], 'd']

fruit = my_list[6]
print(fruit)
print(fruit[2])

print(my_list[6][2])
print(my_list[6][1][1])

# if lists get this complex, there's probably a better way to do it

my_list[6][2]=['cavendis','local']
print(my_list[6][2][1])
