# "immutable"     can't be changed
# strings can't be changed, they can only be reassigned

keys = "qwertz"

# not possible
# keys[5]="y"

keys = keys[0:5] + "y"
print(keys)
