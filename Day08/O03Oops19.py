
class Animal:
    def __init__(self):
        self.a = 10
        print("Animal Ctor.....")

    def eat(self):
        print("Animals eat......")

    def fun(self):
        print("fun method of Animal Class")

class Person:
    def __init__(self):
        self.p = 20
        print("Person Ctor.........")

    def Talk(self):
        print('Persp')

    def fun(self):
        print("fun method of Person class")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()          # call parent class
        Person.__init__(self)
        self.g = 30
        print("Girl Ctor")

    def Walk(self):
        print('Girls Walk.....')

jeni = Girl()
jeni.eat()
jeni.Walk()

jeni.fun()          # ?

print("-" * 60)
print(jeni.__dict__)