# assigning values:         =
# comparing values:         ==
# smaller / larger than:    < / >
# smaller than or equal:    <=
# 'bang', not equal to:     !=
# or before and
# but use () anyways ...
# not

print(10 == 10)               # returns True
print(10 == 9)                # returns False

print('hello' == 'Hello'.lower())

print(10 == '10')             # returns False, type
print(10 == 10.00)            # returns True, because ... it's kind of true. 'truthy'

print(10>5)

print( 10 != 5 )

print( 'hello' == 'Hello' or 5 == 5)
print( 'hello' == 'Hello' and 5 == 5)
print( 'hello' == 'hello' and 5 == 5)

# not neccessary but it's just nicer: ()

print( ('hello' == 'Hello') or (5 == 6) and True)

print( ('hello' == 'Hello') or (5 == 5) and ('8' != '8'))
print( (('hello' == 'Hello') or (5 == 5)) and ('8' != '8'))

print(not 5)
print(not False)
print(not True)
print(not 0)
print(not 1)

condition = not ( 5 == 5 )
print(type(condition))
