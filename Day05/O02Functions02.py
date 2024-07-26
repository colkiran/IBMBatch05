
from collections import namedtuple
# immutable dict or creating a class using functions

def Results(hlno):
    sc = 89
    ss = 90
    mat = 95
    lan1 = 76
    lan2 = 80
    nmdTpl = namedtuple("Marks", "gs st mt l1 l2")
    marks = nmdTpl(gs = sc, st = ss, mt=mat, l1 = lan1, l2 = lan2)
    return marks

mrks = Results(923498)
# print(mrks)
print(f"Science    :{mrks.gs}")
print(f"Social     :{mrks.st}")
print(f"Maths      :{mrks.mt}")
print(f"Language 1 :{mrks.l1}")
print(f"language 2 :{mrks.l2}")


