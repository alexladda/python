# in Python functions are first-class objects
# that means they can be passed around like any other object (int, str, list)

def one_more(my_int):
    return my_int + 1


def two_more(my_int):
    return my_int + 2


def let_me_see(something):
    return something(38)


def i_want_to_see_everything(something1, something2):
    return something1(38), something2(38)


print(let_me_see(two_more))
print(let_me_see(one_more))
print(i_want_to_see_everything(one_more, two_more))


def first_name(my_str):
    return my_str.lower()


def last_name(my_str):
    return my_str.upper()


def pretty(name_func, your_name):
    return name_func(your_name)


def whole_name(first_name_func, first_name, last_name_func, last_name):
    return (first_name_func(first_name), last_name_func(last_name))


print(pretty(first_name, "Alex"))
print(pretty(last_name, "Ladda"))
print(whole_name(first_name, "ALEX", last_name, "LADDA"))
