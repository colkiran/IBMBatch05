

def outerFun(gname):
    gnm = "Mr." +  gname
    def innerFun():

        print("Hello World...")
        print(f"Greetings {gname}")

    return innerFun

# res is reference to innerfun
res = outerFun("Sachin")

st = "Hello World"
print(st[0:])
print(st[::-1])

# after few lines of code
res()

print("-" * 60)
outerFun("Rahul")()        # calls the innerFun





#-------------------------
# def sum(x, y):
#     return x + y
#
#
# res = sum(10, 20)
# print(res)



