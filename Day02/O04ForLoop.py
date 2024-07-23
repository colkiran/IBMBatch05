
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(1, 15, 2):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(2, 15, 2):
    print(i, end=" ")
print()

print("-" * 60)
for i in range(10, 101, 10):
    print(i, end=" ")
print()

print("-" * 60)
for i in range(1, 31):
    # if i > 20:
    #     break
    if i % 2 == 1:
        continue
    print(i, end=" ")
else:
    print("\nIteration completed.....")

print("-" * 60)

for i in range(1, 11):
    for j in range(i):
        print(j, end=" ")
    print()




