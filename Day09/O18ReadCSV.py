
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as csvFile:
    emp_details = csv.reader(csvFile)
    prtyTbl = PrettyTable(next(emp_details))
    
    for line in emp_details:
        prtyTbl.add_row(line)

print(prtyTbl)



"""
    colnames = next(emp_details)
    print(*colnames)

    for line in emp_details:
        print(*line)
"""
