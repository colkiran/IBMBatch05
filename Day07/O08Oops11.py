
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular', 'React']

    def __str__(self):
        return "Name is {} and salary is {}".format(self.name, self.salary)

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val


emp1 = Employee("John", 25000)
print(emp1)

print("-" * 60)

print([emp for emp in emp1])

print("-" * 60)

print(len(emp1))

print("-" * 60)

emp1.append("Python")
print([emp for emp in emp1])

print("-" * 60)
res = emp1[5]
print(f"res :{res}")

print("-" * 60)
emp1[3] = "JSP"
print([emp for emp in emp1])
