"""
sort    - sort will sort the original list, so it does not return              anything
sorted  - sorted will create a copy of the list sorts it and returns           it as a result
"""

print("sort".center(60, "-"))
l1 = [8, 5, 9, 1, 6, 10, 4, 7, 3, 2]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending Order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending Order :{res_desc}")

print("-" * 60)
l1 = (8,'zebra', 'apple', 5, 'xray', 'blue', 9, 'white', 'green', 1, 'violet', 'pink', 6, 'orange', 'maroon', 10, 'cat', 'yellow', 4, 'dog', 'egg', 7, 'queen', 3, 'king', 2, 189, 1451, 29, 260, 2432 )

print(f"l1 :{l1}")
print("-" * 60)

res = sorted(l1, key=ascii)
print(f"res :{res}")

for i in range(0, len(l1)):
    if type(res[i]) == int:
        print(i)
        break

print(res[0:16] + sorted(res[16:]))

print("-" * 60)

cities = ['thiruvananthapuram', 'bangalore', 'pune', 'hyderabad', 'mumbai', 'vishakapatnam', 'madurai', 'delhi', 'ooty', 'kolkota']

print(f"cities :{cities}")
# sort the cities depending on the length of their names

print("-" * 60)
res = sorted(cities, key=len)
print(f"res :{res}")

print("reverse".center(60, "-"))
l1 = [8, 5, 9, 1, 6, 10, 4, 7, 3, 2]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")
