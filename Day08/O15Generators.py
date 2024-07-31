
l1 = [x ** 2 for x in range(1, 11)]
print(f'l1 :{l1}')
print(type(l1))

print("-" * 60)
l1 = (x ** 2 for x in range(1, 11))
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
s1 = sum([x ** 2 for x in range(1, 11)])
print(f"Sum of squares using comprehension :{s1}")

print("-" * 60)
s2 = sum((x ** 2 for x in range(1, 11)))
print(f"Sum of squares using generator :{s2}")

print("-" * 60)
from sys import getsizeof

t1 = [x ** 2 for x in range(1, 10000)]
print(f"Comprehension size of the list :{getsizeof(t1)}")

t2 = (x ** 2 for x in range(1, 10000))
print(f"Generator size of the list :{getsizeof(t2)}")
