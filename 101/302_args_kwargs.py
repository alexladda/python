# args              arguments
# kwargs            key word arguments
# kwargs()              returns dict
# kwargs.keys()         returns all keys
# kwargs.values()       returns all values
# kwargs.get('key')     returns value for 'key'

def my_sum(*args):
    return sum(args)
sum_2 = my_sum(1,23,1,23,4,3,3,3,3,23)
print(sum_2)

def my_sum(*numbers):
    return sum(numbers)
sum_2 = my_sum(1,23,1,23,4,3,3,3,3,23)
print(sum_2)

sum_1 = sum((1,2,3,4,5))
print(sum_1)

def key_value_func(**kwargs):
    return(kwargs)
key_value_1 = key_value_func(house="bad", apartment="good")
print(key_value_1, type(key_value_1), sep=' - ')

def key_value_func(**kwargs):
    return(kwargs.keys())
key_value_1 = key_value_func(house="bad", apartment="good")
print(key_value_1, type(key_value_1), sep=' - ')

def key_value_func(**kwargs):
    return(kwargs.values())
key_value_1 = key_value_func(house="bad", apartment="good")
print(key_value_1, type(key_value_1), sep=' - ')

def key_value_func(**kwargs):
    return(kwargs.get("house"))
key_value_1 = key_value_func(house="bad", apartment="good")
print(key_value_1, type(key_value_1), sep=' - ')
