employees = {
    'mike': 27000,
    'john': 65000,
    'rebecca': 60000,
    'tom': 100000
}

for person in employees:
    print(person, " (- by default)")      # returns the keys (by default)

for person in employees.keys():
    print(person,  " (- explicitly)")     # returns the keys explicitly

for entry in employees.values():
    print(type(entry), end=": ")
    print(entry)                          # returns the values for each key


print(type(employees.items()), end=": ")  # returns dict_items object
print(employees.items())                  # with a list of tuples (key,value)
for entry in employees.items():
    print(type(entry), end=": ")          # returns a tuple
    print(entry)                          # with key and item

for entry in employees.items():
    print(entry[0] + " earns " + str(entry[1]))

for name, salary in employees.items():
    print(name + " earns " + str(salary))

for (name, salary) in employees.items():    # basically defining a literal tuple
    print(name + " earns " + str(salary))

# this procedure is called unpacking

# now with a list of tuples
print("now with a list of tuples")
employees = [
    ('mike', 27000),
    ('john', 65000),
    ('rebecca', 60000),
    ('tom', 100000)
    ]
for (name, salary) in employees:            # items only for dictionaries
    print(name + " earns " + str(salary))



# three values in the tuple
print("three values in the tuple")
employees = [
    ('mike', 27000, 28),
    ('john', 65000, 39),
    ('rebecca', 60000, 21),
    ('tom', 100000, 62)
    ]

for (name, salary, age) in employees:            # items only for dictionaries
    print(name + " earns " + str(salary) + " at the age of " + str(age))
