
def fib(x):
    if x == 1 or x == 0:
        return x
    else:
        return fib(x - 1) + fib(x - 2)

n = int(input("Enter the fibanocci series to be generated :"))
for i in range(n):
    print(fib(i), end=" ")
print()
