
import numpy as np

arr = np.array([1, 2, 3, 4])
print(f"arr \n:{arr}")
print(arr.dtype)

print("-" * 60)
arr1 = np.array(['apple', 'orange', 'banana'])
print(f"arr1 \n:{arr1}")
print(arr1.dtype)

print("-" * 60)
arr2= np.array([1, 2, 3, 4, 5], dtype="S")
print(arr2)
print(arr2.dtype)

print("-" * 60)
arr2= np.array([1, 2, 3, 4, 5], dtype="i4")
print(arr2)
print(arr2.dtype)

print("-" * 60)
arr4 = np.array([1.0, 2.3, 3.1, 4.5])
print(arr4)

newarr = arr4.astype("i")
print(newarr)
print(newarr.dtype)