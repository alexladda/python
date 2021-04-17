# functions inside other functions

def level_zero():
    print("this is level 0")

    def next_level():
        print("this is the next level")

    def first_level():
        print("this is the first level")

    next_level()
    first_level()


level_zero()
