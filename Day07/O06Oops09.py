from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # this works even for != (not equal to)
    def __eq__(self, other):
        return self.salary == other.salary

    # this works for less than also
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Kevin", 95000)
print(emp1)

print("-" * 60)

emp2 = Employee("Peter", 90000)
print(emp2)

print("-" * 60)

# compares the addresses by default
if emp1 != emp2:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is  equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

if emp1 < emp2:
    print("{} salary of {} is less than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is less than {} salary of {}".format(emp2.name, emp2.salary, emp1.name, emp1.salary))

print("-" * 60)

print(emp1 >= emp2)
print(emp1 <= emp2)
