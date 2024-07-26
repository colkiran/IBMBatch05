
def outerFun():
    gname = "Sachin"
    def innerFun():
        nonlocal gname          # only local variable can be converted                              into non local variables
        gname = "Mr." + gname
        print("Hello World")
        print(f"Greetings {gname}")

    # outer fun scope
    innerFun()
    print(f"Outside :{gname}")

outerFun()
