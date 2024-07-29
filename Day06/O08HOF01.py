
def fun(*args):
    print(args)

fun()
fun(1)
fun(1, 2)
fun(1,2,3)
fun(1,2,3,4)

print("-" * 60)

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def outerFun(fnc):              # HOF
    lofInfo = "Logging into the system...."

    def innerFun(*args):
        print(lofInfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

sum_logger = outerFun(sum)
diff_logger = outerFun(diff)

sum_logger(20, 40)
diff_logger(60, 29)
