
def outerFun():
    gname = "Sachin"            # local variable

    def innerFun():
        nonlocal gname          # only local variables can be                               converted to non local variables
        gname = "Mr." + gname

        print("Hello World")
        print(f"Greetings {gname}")

    # outerfun scope
    innerFun()
    print(f"Outside :{gname}")

outerFun()
