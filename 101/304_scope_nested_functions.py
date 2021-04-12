# global scope
# local scope

age = 27
print(age)

def increase_age():
    age = 30
    def add_4_to_age(age):   # age needs to be passed in specifically
        age = age + 4
        print("NESTED FUNCTION: " + str(age))
    add_4_to_age(22)
    add_4_to_age(age)

increase_age()




print(age)
