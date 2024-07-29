
class Player:

    def __init__(self):
        self.name = "Sachin"            # instance vars or member vars
        self.age = 32
        print("Player Initialized......")

    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}")

ply1 = Player()
ply1.get_details()
print('-' * 60)

ply2 = Player()

# Python supports
ply2.name = "Sourav"
ply2.age = 30

ply2.get_details()

