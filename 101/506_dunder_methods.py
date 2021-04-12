class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        print(Employee_Object) will look for this function if called.
        """
        return self.name + " is this old: " + str(self.age)

    def __len__(self):
        return self.age

tom = Employee("Tom Lanister", 47)
print(tom)
print(tom.__str__())

print(len(tom))
print(tom.__len__())
