# you can't / shouldn't create an object from an abstract class
# it's only supposed to be inherited from.

class Animal:
    def __init__(self, name):
        self.animal_name = name

    def eat(self):
        raise NotImplementedError("Child class should be implementing this")

class Monkey(Animal):
    def eat(self):
        print("monkey eating bananas ...")

class Bird(Animal):
    def eat(self):
        print("bird eating seeds ...")
    def fly(self):
        print("bird soaring high")



myMonkey = Monkey('jojo')
myMonkey.eat()

myBird = Bird('tim')
myBird.fly()
