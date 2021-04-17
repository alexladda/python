# the magical beast

def nice_and_plushy(func):
    def wrapper():
        print("*********** ")
        func()
        print("*********** ")
    return wrapper


def blonk():
    print("blonk!")


# called directly
nice_and_plushy(blonk)()

# or passed into another function
a = nice_and_plushy(blonk)
a()
