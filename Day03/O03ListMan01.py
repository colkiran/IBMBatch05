
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.1, 6.9, 7.2, 8 + 2j, 9 - 2j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3= list(range(1, 11))
print(f'l3 :{l3}')

print("-" * 60)
# CRUD operation
# create
l1 = list(range(1, 6))
print(f"l1 :{l1}")

print("-" * 60)
# read
print(f"l1[0]  :{l1[0]}")
print(f"l1[-1] :{l1[-1]}")
print(f"l1[0:3] :{l1[0:3]}")

# iterate
for i in l1:
    print(i, end=" ")
print()

for i in range(0, len(l1)):
    print(l1[i], end = " ")
print()

print("-" * 60)
# updation - modify the existing values or insert new values
print(f"l1 :{l1}")

# modify
l1[2] = 300
l1[-2] = 400
print(f"l1 :{l1}")

# insert
l1[3] = 350
print(f"l1 :{l1}")

# python lists are static, so we cannot add new values into the list

print("-" * 60)
# delete
print(f"l1 :{l1}")

del l1[2]
del l1[-3]

print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))