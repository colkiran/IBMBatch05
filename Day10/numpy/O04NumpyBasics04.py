
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr[1:5])
print(arr[1:5:2])

# alternate elements from the array
print(arr[::2])

print("two dimension".center(60, "-"))

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"arr2 \n:{arr2}")

print("-" * 60)

print(arr2[1, 1:4])
print("-" * 60)

print(arr2[0:2, 2])
print("-" * 60)

print(arr2[0:2, 1:4])
