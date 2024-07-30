
# Arithmetic Operator Loading

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name} \n salary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary



ply1 = Employee("Robin", 560000)
ply2 = Employee("Kennedy", 8500)

# Add
print(f"Add :ply1 + ply2 :{ply1 + ply2 }")

# sub
print(f"Sub ply - ply2 :{ply1 - ply2}")

# multuply
print(f"Multiply- ply1 * ply2 {ply1  * ply2}" )

# division
print(f"Divide - ply1 / pl1y2 :{ply1 / ply2}")

# floor div
print(f"FloorDiv - ply1 // ply2 :{ply1 // ply2}")








