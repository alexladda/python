
word = "hello"
my_list = list(word)
print(my_list)
my_list = []

for character in word:
    print(character)

for num in range(2,11,2): # start, stop, step size
    print(num)

my_num = [1,2,3,4,5,6,7,8,9]
words = ['hello', 'my', 'name', 'is', 'alex']

combined_items = zip(my_num, words) # ignores values that can't be matched
print(type(combined_items))
print(combined_items)

for item in combined_items:
    print(item)


words = ['hello', 'my', 'name', 'is', 'alex']
for item in enumerate(words, 1001):
    print(item)

my_dict = dict(enumerate(words))
print(my_dict)
