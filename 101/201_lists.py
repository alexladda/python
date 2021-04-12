# lists are mutable

my_list=[1,2,3,4,5]
print(my_list)
print(type(my_list))


my_list.pop()                           # lists are mutable
print(my_list)

my_list.pop(0)
print(my_list)

my_list[0] = 'S'
print(my_list)
print(type(my_list[0]))
print(type(my_list[1]))

my_list[0] = ['hello', 'goodbye']       # lists can contain lists
print(my_list)

my_list.append('this is a sentence')    # you can append exactly 1 item
print(my_list)                          # this won't work: my_list.append(8,9,10)



print(my_list.pop(0))                   # .pop() returns the popped item
print(my_list.append('appended item'))  # .append() returns None
print(my_list)

#my_list.sort()  # error because mixed types

my_list.pop(2)
my_list.pop(2)
my_list.sort()  # sorts ascending
my_list.reverse()
print(my_list)

my_list=[   'Beautiful is better than ugly.',
            'Explicit is better than implicit.',
            'Simple is better than complex.',
            'Complex is better than complicated.',
            'Flat is better than nested.',
            'Sparse is better than dense.',
            'Readability counts.',
            'Special cases aren\'t special enough to break the rules.',
            'Although practicality beats purity.',
            'Errors should never pass silently.',
            'Unless explicitly silenced.',
            'In the face of ambiguity, refuse the temptation to guess.',
            'There should be one-- and preferably only one --obvious way to do it.',
            'Although that way may not be obvious at first unless you\'re Dutch.',
            'Now is better than never.',
            'Although never is often better than *right* now.',
            'If the implementation is hard to explain, it\'s a bad idea.',
            'If the implementation is easy to explain, it may be a good idea.',
            'Namespaces are one honking great idea -- let\'s do more of those!']

my_list.sort()
print(my_list)
print(my_list[5:8])                 # lists are slicable

poem_length = len(my_list)
print('This poem has ' + str(poem_length) + ' sentences')
sentence_length = len(my_list[0])
print('This fist sentence has ' + str(sentence_length) + ' characters')
length_of_length = len(str(sentence_length))
print('This does not make too much sense anymore: ' + str(length_of_length))

other_list=[
'Shall I compare thee to a summer’s day?',
'Thou art more lovely and more temperate:',
'Rough winds do shake the darling buds of May,',
'And summer’s lease hath all too short a date;',
'Sometime too hot the eye of heaven shines,',
'And often is his gold complexion dimm\'d;',
'And every fair from fair sometime declines,',
'By chance or nature’s changing course untrimm\'d;',
'But thy eternal summer shall not fade,',
'Nor lose possession of that fair thou ow’st;',
'Nor shall death brag thou wander’st in his shade,',
'When in eternal lines to time thou grow’st:',
'   So long as men can breathe or eyes can see,',
'   So long lives this, and this gives life to thee.'
]

print(my_list + other_list)
