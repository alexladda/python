# tuples are immutable

my_tuple = (1,2,3,'some data', [1,2,3])
my_list = [1,2,3,'some data', [1,2,3]]
print(my_tuple[4])

# my_tuple[3] = "other data"
# my_tuple[4] = ['a', 'b', 'c']
# 'tuple' object does not support item assignment

my_tuple[4][0] = 'a'
print(my_tuple)

# list values within tuples can be changed but not the list item itself

my_tuple[4].append('a')
print(my_tuple)

print(type(my_tuple[0:2]))         # sliced tuple returns tuple
my_list = [1,2,3,'some data', [1,2,3]]
my_list = [my_tuple[0:]]
print(type(my_list[0:2]))          # sliced list returns list

extracted_list = my_tuple[4]
print(type(extracted_list))
