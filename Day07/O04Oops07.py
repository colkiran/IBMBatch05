
class Player:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        print(f"Ctor called......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}\nRuns score d is {self.score}")

    @staticmethod
    def StrikeRate(runs, balls):
        return (round((runs / balls) * 100), 2)


ply1 = Player("Virat", 34, 150)
ply1.get_details()
print("Strike Rate is :", Player.StrikeRate(150, 89))








