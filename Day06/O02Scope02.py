
# local Scope

def fun(x):             # x- local variable
    y = "hello world"   # y - local variable
    print(f"Inside x :{x}")
    print(f"Inside y :{y}")


fun(100)
# print(f"Outside x :{x}")
# print(f"Outside y :{y}")

