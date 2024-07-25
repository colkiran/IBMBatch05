
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print('-' * 60)
d2 = {'name': 'sachin', 'age': 29, 'runs': 120, 'oppn': "WI"}
print(f"d2 :{d2}")
print(type(d2))

print('-' * 60)
d3 = dict([('name', 'John'), ('class', "9th"), ('age', 14), ('school', 'NPS')])
print(f"d3 :{d3}")
print(type(d3))

print('-' * 60)
d4 = dict(name="Messi", age=37, goals=500, country="Argentina")
print(f"d4 :{d4}")
print(type(d4))

print('-' * 60)
# CRUD
# create
player = {'name': 'Sachin', 'age': 32, 'runs': 85, 'oppn': 'Aus'}
print(f"player :{player}")

print('-' * 60)
# read
print(f"Name     :{player['name']}")
print(f"Age      :{player['age']}")
print(f"opponent :{player['oppn']}")

print('-' * 60)
for i in player:
    print(i, "=>", player[i])

print('-' * 60)
# Update - Modify, add new key: value
# modify

print(f"player :{player}")

player['name'] = "Tendulkar"
player['runs'] = 140
print(f"player :{player}")

# add new key: value
player['year'] = '2004'
player['venue'] = 'perth'
print(f"player :{player}")

print('-' * 60)
# delete
print(f"player :{player}")

del player['age']
del player['year']

print(f"player :{player}")

print('-' * 60)
print(dir(player))
