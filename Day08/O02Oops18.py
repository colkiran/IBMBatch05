
class Animal:

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("Birds fly....")

class Chicken(Bird):

    def msg(self):
        print("Chickens are breded for consumption")

    def fly(self):
        print(f"Chickens Seldom Fly")

chick = Chicken()
chick.eat()
chick.fly()
chick.msg()