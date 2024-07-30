
class Employee:

    def __init__(self, name):
        self.__name = name          # private variable
        self.tech = ['C', 'C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular', 'React']

    def __str__(self):
        return self.__name + " " + ", ".join([str(v) for v in self.tech])

emp1 = Employee("Stuart")
print(emp1)

print('-' * 60)

# print(emp1.__name)
print(emp1.__dict__)
emp1._Employee__name = "Ben"

print('-' * 60)
print(emp1)

print('-' * 60)
print(emp1.__dict__)
