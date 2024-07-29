
def outerFun(greet):        # HOF - Higher order function

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")
print("-" * 60)

ref = outerFun("Welcome")
ref("Rahul")
ref("Virat")

print("-" * 60)
tmlGrt = outerFun("Vanakam")
kanGrt = outerFun("Namaskara")

tmlGrt("Ashwin")
kanGrt("Rahul")
