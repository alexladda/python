def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@do_twice
def hello(word):
    print("hello", word)


def go_on(func):
    def wrapper(*args, **kwargs):
        n = args[0]
        print(n)
        n += 1
        func(n)
        n += 1
        func(n)
    return wrapper


@go_on
def start(number):
    print(number)


hello("world")


go_on(start(1231))
