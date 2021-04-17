# a function can return a can return function

def level_zero(request):

    def next_level():
        print("this is the next level")

    def first_level():
        print("this is the first level")

    if request == "next":
        return next_level
    elif request == "first":
        return first_level
    else:
        print("ok bye.")


x = input("where do you want to go? ")


level = level_zero(x)
print(level)

# now we can use them as functions...
# normally they would only be locally defined in the parent functions
# this way we can get out the child functions

level()
