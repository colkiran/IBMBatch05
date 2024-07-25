
print("copy".center(60, "-"))
ply1 = {'name': 'Sachin', 'age': 32, 'runs': 150, 'oppn': 'WI'}
print(f"ply1 before :{ply1}")

# copy the dictionary ply1 to ply2
ply2 = ply1     # shallow copy - copies the data with the address
print(f"ply2 before :{ply2}")

ply2['venue'] = 'Sabina Park'
ply2['cntry'] = 'India'

print(f"ply2 after :{ply2}")
print(f"ply1 after :{ply1}")

print("=" * 60)
print("=" * 60)

ply3 = {'name': 'Rahul', 'age': 30, 'runs': 45, 'oppn': 'Pak'}
print(f"ply3 before :{ply3}")

# copy the dictionary ply3 to ply2
ply4 = ply3.copy()
print(f"ply4 before :{ply4}")

ply4['cntry'] = "India"
ply4['year'] = 2010

print(f"ply4 after :{ply4}")
print(f"ply3 after :{ply3}")

print("=" * 60)
print("=" * 60)

ply5 = {'name': 'Rahul', 'age': 30, 'runs': {'pak':45, 'sri':67}, 'series': 'asia cup'}
print(f"ply5 before :{ply5}")

# copy the dictionary ply5 to ply6
ply6 = ply5.copy()      # deep copy - only data gets copied
print(f"ply6 before :{ply6}")

ply6['runs']['afg'] = 85
ply6['runs']['bgl'] = 55

print(f"ply6 after :{ply6}")
print(F"ply5 after :{ply5}")

print("=" * 60)
print("=" * 60)

ply7 = {'name': 'Yuvraj', 'age': 30, 'runs': {'pak':125, 'sri':67}, 'series': 'asia cup'}
print(f"ply7 before :{ply7}")

# copy the dictionary ply7 to ply8
from copy import deepcopy
ply8 = deepcopy(ply7)

print(f"ply8 before :{ply8}")

ply8['runs']['afg'] = 89
ply8['runs']['bgl'] = 105

print(f"ply8 after :{ply8}")
print(f"ply7 after :{ply7}")