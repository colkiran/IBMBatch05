
def add(x, y):
    return x + y

# res = add(100, 200)
# print(f"res :{res}")
a = add

res = a(45, 56)
print(f"res :{res}")

print("-" * 60)

b = lambda x, y: x + y

res = b(30, 50)
print(f"res :{res}")

print("-" * 60)
"""
 lambdas are best used with 
  1. map  = map(lambda, list)
  2. filter = filter(lambda, list)
  3. reduce = = reduce(lambda, list)
"""
print("map".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x: x ** 2, l1))
print(f"squares :{squares}")

# most of the examples - conversions - rs - $, kgs - pounds, celsius -

# in rs
expneses = [45000, 175000, 250000, 80000, 500000, 345000]

# convert it into dollars (83.7)
res = list(map(lambda x: round(x / 83.7,2), expneses))
print(f"res :{res}")

print("-" * 60)

months = ['oct', 'jul', 'dec', 'aug', 'nov', 'sep', 'jan', 'apr', 'feb', 'jun', 'mar', 'may']

print(f"unsorted months :{months}")
print("-" * 60)
# sort these months
from calendar import month_abbr
# print(f"month_abbr :{list(month_abbr)}")

sorted_months = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print(f"Sorted Months :{sorted_months}")

print("filter".center(60, "-"))
# lambda expression should return a True or False

l1 = list(range(1, 26))
print(f"l1 :{l1}")

mul_of_3 = list(filter(lambda x : x % 3 == 0, l1))
print(f"multiples of 3 :{mul_of_3}")

sentence = "the quick brown fox jumps over the lazy dog"
res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")

print("reduce".center(60,  "-"))
from functools import reduce

l1 = [9, 7, 2, 3, 6, 8, 10, 5, 1, 4]
print(f"l1 :{l1}")

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

res = reduce(lambda x, y : x + y, l1)
print(f"res :{res}")
