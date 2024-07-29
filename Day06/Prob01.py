
import time
def timeCalc(fnc):

    def helper(secs):
        print("Starting to Execute ......")
        st = time.perf_counter()
        fnc(secs)
        et = time.perf_counter()
        print("Completed executing.....")
        print(f"It took {round(et-st, 2)} secs to complete the task......")

    return helper


@timeCalc
def fun(arg):
    lst = list()
    for i in range(1, arg+1):
        for j in range(i):
            lst.append(j ** 2)

fun(7500)

# write a decorator to find the time taken by the function fun to execute
