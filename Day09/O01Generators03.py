
def fun():
    x = 1
    print("Apples from ooty....")
    yield x
    x += 9
    print("Oranges from Kanpur......")
    yield x
    x += 10
    print("Grapes from Hubli......")
    yield x

res = fun()
print(f"res :{res}")

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

def fun():
    for i in range(1, 11):
        yield i

print("-" * 60)

genObj = fun()

print(genObj.__next__())
print(genObj.__next__())
print(genObj.__next__())

print("-" * 60)
for x in fun():
    print(x, end=" ")
print()






