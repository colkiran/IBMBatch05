
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):

            from emojis import emojis
            emojized = emojis.encode("Greetings" + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

kanGrt = outerFun("Namaskara")
KtgrGrt = kanGrt("tiger")
KtgrGrt("Prabhakar")




"""
engGrt = outerFun("Welcome")
EsngArw = engGrt("----->")

tmlGtr = outerFun("Vanakam")
TsngArw = tmlGtr("----->")

EsngArw("Sachin")
TsngArw("Sachin")
"""