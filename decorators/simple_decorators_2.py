from datetime import datetime


def not_in_the_night(func):
    def wrapper():
        if 22 <= datetime.now().hour < 7:
            func()
        else:
            print("psst.")
    return wrapper


def be_loud():
    print("blonk!")


blonk = not_in_the_night(be_loud)

blonk()
