
glbX = 100

def fun(i):   # i is a local variable
    global glbX         # do not assign any val to glbX in this line
    print(f"i :{i}")
    glbX = 500
    print(f"Inside {glbX}")


print(f"Before :{glbX}")

fun(10)

print(f"After  :{glbX}")
