
print("append".center(60, "-"))
l1 = list(range(6, 11))
print(f"l1 :{l1}")

l1.append(11)
l1.append(12)
l1.append(13)

print(f"l1 :{l1}")

l1.append([14, 15, 16, 17, 18])
print(f"l1 :{l1}")
print(f"l1[-1][1:4] :{l1[-1][1:4]}")
# l1 :[6, 7, 8, 9, 10, 11, 12, 13, [14, 15, 16, 17, 18]]

print("extend".center(60, "-"))
l2 = [2, 4, 6, 8, 10]
print(f"l2 :{l2}")

l2.extend([12, 14, 16, 18])
print(f"l2 :{l2}")

l = [20, 22, 24]
l2.extend(l)
print(f"l2 :{l2}")

l2.extend([26])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

l1.insert(15, 20)
print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.remove(1)
l1.remove(3)
l1.remove(5)
print(f"l1 :{l1}")

# l1.remove(1) - throws a error if the number is not in the list

l1 = [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2 ]

while 2 in l1:
    l1.remove(2)

print(f"l1 :{l1}")
