
import sys

# print(sys.path)     # list
sys.path.append("C:\\Delhi")

print([path for path in sys.path])

import gurgaon.mymodule as m

print(m.gname)

m.greet("Kapil Dev")

emp1 = m.Employee("Mike", 320000)
print(emp1)
