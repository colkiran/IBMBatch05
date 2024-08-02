
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"arr :{arr}")
print(type(arr))

print(arr.ndim)

print("arr \n", arr)
print("first row and second element :", arr[0, 1])
print("second row and third element :", arr[1, 2])

print("-" * 60)

arr3 = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(f"arr3 \n :{arr3}")

print(arr3[0, 1, 2])
print(arr3[1, 0, 1])