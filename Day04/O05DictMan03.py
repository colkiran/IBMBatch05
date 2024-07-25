
print("setdefault".center(60, "-"))
player = {'name': 'Sachin Tendulkar', 'age': 32, 'runs': 98, 'oppn': 'NZL'}
print(f"player :{player}")

player.setdefault('name', 'Rahul')
player.setdefault('runs', 150)

player.setdefault('country', 'India')
player.setdefault('venue', 'Auckland')

print(f"player :{player}")

print("pop".center(60, "-"))
emp = {'name' :'Steve', 'age': 34, 'desig': 'MGR', 'dept': 'HR', 'loc': 'Che', 'sal': 145000}

print(f"emp :{emp}")

res = emp.pop('dept')
print(f"res :{res}")

res = emp.pop("age")
print(f"res :{res}")

# res = emp.pop()

print(f"emp :{emp}")

print("popitem".center(60, "-"))

emp = {'name' :'Steve', 'age': 34, 'desig': 'MGR', 'dept': 'HR', 'loc': 'Che', 'sal': 145000}

print(f"emp :{emp}")

res = emp.popitem()
print(f"res :{res}")

res = emp.popitem()
print(f"res :{res}")

print(f"emp :{emp}")

print("clear".center(60, "-"))

emp = {'name' :'Steve', 'age': 34, 'desig': 'MGR', 'dept': 'HR', 'loc': 'Che', 'sal': 145000}

print(f"emp :{emp}")

emp.clear()

print(f"emp :{emp}")

print("update".center(60, "-"))

emp1 = {'name' :'Steve', 'age': 34, 'desig': 'MGR', 'dept': 'HR', 'loc': 'Che'}

print(f"emp1 :{emp1}")

emp2= {'name' :'George', 'age': 45, 'desig': 'VP', 'loc': 'Hyd', 'sal': 180000}
print(f"emp2 :{emp2}")

# update emp1 with emp2 values
emp1.update(emp2)
print(f"emp1 :{emp1}")
