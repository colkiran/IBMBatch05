
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.age = 1

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def __init__(self):         # overiding the parent class Ctor
        super().__init__()      # calls the parent class constructor
        print('Bird Ctor....')
        self.weight = '1k'

    def fly(self):
        print("Birds Fly.....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)

print(cuckoo.__dict__)