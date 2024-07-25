
print("get".center(60, "-"))
player = {'name': 'Cristiano Ronaldo', 'age':38, 'ballandors': 5, 'club': 'Al-Nassr FC', 'goals': 600}
print(f"player :{player}")

print(f"Name :{player.get('name', 'Invalid Key, Please Enter a valid key....')}")
print(f"Club :{player.get('Club', 'Invalid Key, Please Enter a valid key....')}")

print("Keys".center(60, "-"))
player = {'name' :"Lionel Messi", 'age': 37, 'ballandors': 8, 'club': 'Inter Miami', 'goals': 550}
print(f"player :{player}")

kys = player.keys()
print(f"Keys :{kys}")

print("-" * 60)
for ky in player.keys():
    print(ky + " => " + str(player[ky]))

print("values".center(60, "-"))
vls = player.values()

print(f"Values :{vls}")

for v in vls:
    print(v, end=" ")
print()

print("items".center(60, "-"))
# combination of keys and values - it returns keys and values
print(f"player :{player}")

print("-" * 60)
for k, v in player.items():
    print(k, "=>", v)

print("-" * 60)
emp = {
    'emp1': {'name' :'Steve', 'age': 34, 'desig': 'MGR', 'dept': 'HR', 'loc': 'Che', 'sal': 145000},
    'emp2': {'name' :'George', 'age': 45, 'desig': 'MGR', 'Finance': 'HR', 'loc': 'Hyd', 'sal': 180000},
    'emp3': {'name' :'Tina', 'age': 30, 'desig': 'TL', 'dept': 'IT', 'loc': 'BLR', 'sal': 120000}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")
print("-" * 60)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("fromkeys".center(60, "-"))
# convert a list into a dictionary
cities = ['blr', 'che', 'hyd', 'del', 'mum', 'kol']
print(f"cities :{cities}")

res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 23)
print(f"res :{res}")
