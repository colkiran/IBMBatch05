
# global scope

glbX = 100

def fun(x):        # var x is a local variable
    # declare a variable with global scope, do not assign any value to this variable
    global glbX

    print(f"local var x :{x}")
    y = "hello variable"        # local variable
    print(f"y :{y}")
    glbX = 500
    print(f"Inside :{glbX}")


print(f"Before :{glbX}")

fun(25)

print(f"After :{glbX}")