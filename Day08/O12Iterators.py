
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")
print(type(l))
# print(dir(l))

# l.__iter__() or iter(l)
iterObj = iter(l)
# print(dir(iterObj))
# __iter__ and __next__ are the protocols of iteration

print("-" * 60)
e1 = iterObj.__next__()
print(f"first :{e1}")

print("-" * 60)
e3 = iterObj.__next__()
print(f"third :{e3}")

print("-" * 60)
e4 = iterObj.__next__()
print(f"fourth :{e4}")

print("-" * 60)
e5 = iterObj.__next__()
print(f"fifth :{e5}")

print("-" * 60)
e2 = iterObj.__next__()
print(f"second :{e2}")

print("-" * 60)
e2 = iterObj.__next__()
print(f"second :{e2}")
