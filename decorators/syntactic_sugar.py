# the @ symbol - "the pie syntax"

def nice_and_plushy(func):
    def wrapper():
        print("*********** ")
        func()
        print("*********** ")
    return wrapper


def aaaaargh(func):
    def wrapper():
        print("XXXXXXXXXXX ")
        func()
        print("XXXXXXXXXXX ")
    return wrapper


def blonk():
    print("blonk!")


def clonk():
    print("clonk!")


clonk()
