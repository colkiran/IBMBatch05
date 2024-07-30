
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Player Initialized......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 60)

ply2 = Player("Sourav", 33)
ply2.get_details()
print("-" * 60)
"""
self - will store the name of the object which made a call to the method.

def get_details(self):      # self = ply1
    print(self.name)        # ply1.name
    print(self.age)         # ply1.age
    
ply1.get_detials()
 
every object will store member variable in a dictionary __dict__
ply1's member variables will be stored in ply1.__dict__

"""
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)
ply2.runs = 150
print("ply2 :", ply2.__dict__)
print("ply1 :", ply1.__dict__)

