# key → value
# dictionaries are mutable

dict = { 'k1': 'some data', 7: 'other data', 7: 'data duplicate', 7: 'another duplicate'}
print(type(dict))

# dictionaries are not position oriented like lists and tuples
# they are key oriented

print(dict['k1'])
print(dict[7])

print(dict)
dict[7] = '7a'
print(dict)

# there seem to be some things going in with duplicates
# let's stick with unique values for now

dict = { 'k1': 'some data', 7: 'other data' }
dict[7] = 'NEW VALUE'
print(dict)

# no sorting dictionaries

people_weight_dict = {'john':134, 'mike':170, 'robert':165}
print(people_weight_dict)
people_weight_dict['john'] = 234
print(people_weight_dict)
print(people_weight_dict.pop('robert')) # requires argument
print(people_weight_dict)
print(people_weight_dict.popitem()) # no argument
print(people_weight_dict)
people_weight_dict.clear()
print(people_weight_dict)
people_weight_dict['alex'] = 165
print(people_weight_dict)

# dictionaries can (also) contain lists and dictionaries

dict = {'parents': ['mom', 'dad'], 'kids': ['sister', 'sister', 'brother']}
dict['grandparents'] = ['oma', 'opa']
print(dict)
print(dict['grandparents'])
print(dict['parents'])
print(dict['kids'])
dict['grandparents1'] = dict.pop('grandparents')    # 'renaming' a key
dict['grandparents2'] = ['nanny', 'poti']           # adding a key
print(dict)

dict = {'john':134, 'mike':170, 'robert':165, 'items' : ['orange', {'k1' : 'some deeply nested value'}], 'tuple': (1,2,3,4,5)}
print(dict['items'][1]['k1'])
my_tuple = dict['tuple']
print(type(my_tuple))
print(my_tuple)
print(type(dict['john']))
print(dict['john'])
