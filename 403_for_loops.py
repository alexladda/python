farm_animals = ['goat', 'horse', 'chicken', 'cow', 'dog']

for animal in farm_animals:
    sentence = animal + " is safe in our farm."
    print(sentence)

farm_animals = ('goat', 'horse', 'chicken', 'cow', 'dog')

counter = 0
for animal in farm_animals:
    counter = counter + 1
    sentence = str(counter) + ". "+ animal + " is safe in our farm."
    print(sentence)

greeting = "hello my name is alex"
for char in greeting:
    if char == "e":
        print("EEEE!")
    elif char == " ":
        continue            # moves on to the next iteration
    elif char == "x":
        break               # stops the iteration
    else:
        print(char)
