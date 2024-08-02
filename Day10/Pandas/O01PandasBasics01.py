import pandas
import pandas as pd

mydataset = {
    'cars': ['BMW', 'Audi', 'Merc'],
    'ratings': [3, 7, 5]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

print("-" * 60)
print(pandas.__version__)
