
# class method

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Ctor called......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def createPlayer(cls, fname, lname, age):
        print("Factory.....")
        # calls the constructor of the class
        return cls(f"{fname + ' ' + lname}", age)

ply1 = Player("Dhoni", 37)
ply1.get_details()

# ply2 name should be accepted like - fname and lname
print("-" * 60)

ply2 = Player.createPlayer("Virat", "Kholi", 31)
ply2.get_details()

