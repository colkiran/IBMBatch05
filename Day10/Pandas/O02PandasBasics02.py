
# series

import pandas as pd

a = [1, 3, 5, 7]

pseries = pd.Series(a)
print(pseries)

print("-" * 60)
# print the first value from the series
print(pseries[0])

print("-" * 60)

a = [1, 3, 5, 7]

psrs = pd.Series(a, index=['i', 'j', 'k', 'l'])
print(psrs)

print(psrs['k'])

print("-" * 60)

calories = {'day1': 450, 'day2': 370, 'day3': 325}
psrs1= pd.Series(calories)

print(psrs1)
