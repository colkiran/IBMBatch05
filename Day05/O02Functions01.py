
def greet():
    print("Greeting Mr.Sachin, Welcome to the event......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.......")

# city is called default argument
# gname is called non default argument
def greetGstCty(gname, city="mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event......")

greet()
print("-" * 60)

greetGst("Sachin")
greetGst("Virat")

print("-" * 60)

greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
def admsn(fname, lname, dob, qlf, gender, cno, mailid, adr, city):
    print(f"Name :{fname + ' ' + lname}")
    print(f"DOB  :{dob}")
    print(f"Qualification :{qlf}")
    print(f"Gender :{gender}")
    print(f"Contact No. :{cno}")
    print(f"Email ID :{mailid}")
    print(f"Address :{adr}")
    print(f"City :{city}")

# Named Arguments
admsn(city="Hyderabad", cno="45474342", gender="Male", adr="8th Cross, 5th Main, Gachibowli", qlf="M tech", fname="Micheal", lname="Slater", mailid="mike@gmail.com", dob="10/05/1990")

print("-" * 60)
# variable length arguments
def productAll(*numbers):       # *args - it can store more than one value
    print(numbers)
    print(*numbers) # unpack
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(productAll(1, 2, 3, 4, 5))

print("-" * 60)

# **kwargs will accept data in the form of a dictionary
def extract_detail(**detail):
    print(detail)
    print("-" * 60)

    for k, v in detail.items():
        print(k, "=>", v)

extract_detail(name="Rahul", age=32, runs=120, oppn="SA", venue="Chepauk")

print("-" * 60)

def add(x, y):
    return x + y

a = 26
b = 67
c = add(a, b)
print(f"The sum of {a} and {b} = {c}")

# recursive calls we mostly depend on return function
# 1. factorial of a number, 2. fibanocci series (recursive calls)
print("-" * 60)

def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
def fun():
    "This is a doc string"
    # This is a comment
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 60)

def fun2(x, y):
    """
    fun2(x, y)
    ----------
    1. function fun2 takes 2 arguments x and y
    2. if x and y are integers then result would be a sum of x and y
    3. if x and y are strings then result would be the concatenation of x and y
    4. if x is an integer and y is a string then the function throws an error
    """

    return x + y

help(fun2)
