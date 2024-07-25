
a = 10
b = 20

def add(x, y):
    return x + y

print(f"The value of a is {a} and b is {b}")
print(f"The sum of {a} and {b} is {a + b}")
print(f"The sum of {a} and {b} is {add(a, b)}")

print("-" * 60)
# C style
gname = "Sachin"
print("The value of a is %i and b is %i" % (a, b))
print("The name of the guest is %s" % (gname))
print("The sum of %i and %i is %i" % (a, b, a+b))
print("Welcome %s with a rating of %.3f, what a %s player" % (gname, 9.69999, 'class'))

print("-" * 60)
# python style
print("The value of a is {} and b is {}".format(a, b))
print("Welcome {gname} what a {adj} player with a rating of {rat}".format(gname="Sachin", adj = "class", rat=9.7))

print("-" * 60)
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("The number {num} {num} {num}".format(num = 36))
print("The number {num} {num:f} {num:b}".format(num = 36))
print("The number {num:10} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36256878023))
print("The number {num:10} {num:f} {num:b}".format(num = 36))

# alignment
print("{num:15} Sachin".format(num = 33))
print("{num:15} Sachin".format(num = "Ramesh"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi
print("{pi:010.2}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))
print("{pi:010.5}".format(pi=pi))

print("{num:>15} Sachin".format(num = "Ramesh"))    # right align
print("{num:^15} Sachin".format(num = "Ramesh"))    # center align
print("{num:<15} Sachin".format(num = "Ramesh"))    # left align

print("Python".center(60, '-'))
print("{txt:-^60}".format(txt="Pyhton"))
