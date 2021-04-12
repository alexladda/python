# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:
class Animal:
    kind_of_animal = "generic animal"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("{0} (a {1}) eats generically".format(self.name, self.kind_of_animal))

class Dog(Animal): # convention: Class Names are Capitalized
    kind_of_animal = "dog"
    def move(self):
        print("{0} (a {1}) is trotting along nicely".format(self.name, self.kind_of_animal))

class Fish(Animal):
    kind_of_animal = "fish"
    def move(self):
        print("{0} (a {1}) is swimming".format(self.name, self.kind_of_animal))

class Bird(Animal):
    kind_of_animal = "bird"
    def move(self):
        print("{0} (a {1}) is soaring high".format(self.name, self.kind_of_animal))



dog1 = Dog("Hati", 4)
dog2 = Dog("Balu", 10)
dog3 = Dog("Kobo", 13)

fish1 = Fish("Mr. Fish", 0.4)
fish2 = Fish("Blubb", 2)
fish3 = Fish("''?''", 0)

bird1 = Bird("Polli", 1)
bird2 = Bird("Mercury", 19)
bird3 = Bird("Malta", 3)

dogs = [dog1, dog2, dog3]
fishes = [fish1, fish2, fish3]
birds = [bird1, bird2, bird3]

animals = [dogs, fishes, birds]

for species in animals:
     for animal in species:
         animal.move()
         animal.eat()





# Solution:
# class Animal:
#     def __init__(self):
#         print("Animal Constructed")
#
#     def move(self):
#         print("Animal Moving...")
#
#     def eat(self):
#         print("Animal Eating...")
#
#
#
# class Bird(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Bird flying...")
#
#
#
# class Fish(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Fish Swimming...")
#
#
# class Dog(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Dog Running ...")
#
# mydog = Dog(3, "wolfy")
# mydog.move()
# mydog.eat()
#
# mydog = Fish(1, "nemo")
# mydog.move()
# mydog.eat()
#
# mydog = Bird(3, "jojo")
# mydog.move()
# mydog.eat()
