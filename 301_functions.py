print('hello', ' - ', 'boom')

# help(print)

print('hello', 'boom', sep=' - ', end='\n')

def greet_person():
    print('Hi, nice to meet you.')
greet_person()

def greet_person(asdf):
    print('Hi, nice to meet you.')
# greet_person()        error, 1 argument required
greet_person(3)

def greet_person(asdf):
    print('Hi,' + asdf + '! nice to meet you.', sep=' ')
greet_person('Alex')

def greet_person(name = 'you'):
    print('hi ' + name + '!')
greet_person()
greet_person('Val')

def greet_person(name = 4):
    print('hi ' + name + '!')
greet_person('Val')             # this runs fine
# greet_person()                # not allowed to concatenate string and print

def greet_person(name = "you"):
    print ("Hello, " + str(name))
greet_person(100)

def greet_person(name = "you"):
    '''
    DOCSTRING: this returns a greeting
    INPUT: name
    OUTPUT: Hello, name!
    '''
    print ("Hello, " + str(name))
# help(greet_person)           # shows DOCSTRING

def remainder(numerator, denominator):
    return (numerator % denominator)
rest = remainder(10,4)
print(rest)
