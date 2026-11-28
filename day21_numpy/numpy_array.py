import numpy as np

import math

#1. pycharm package
# 2. Terminal pip install
#3. import library and place cursor and wait for option to display install library

arr = np.array([1,2,3])

ls = [1,'etl',3]
print(ls)

print("arr details", arr, type(arr), id(arr), arr.__sizeof__())
print("dir methods on arr", dir(arr))


arr2 = np.array([1,19.3,True])
print("arr2 details", arr2, type(arr2))
print("arr[0]", arr2[0], type(arr2[0]))
print("arr[1]", arr2[1], type(arr2[1]))
print("arr[2]", arr2[2], type(arr2[2]))

# str>complex>float>int>bool


arr3 = np.array([1,2,3])

ls = [1,2,3]

print(sum(ls))

print(min(ls))
print(max(ls))

print("arr min", arr3.min())

print("arr3.max()", arr3.max())

arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr4)

print("arr2", arr2)

arr2[2] = 18.5

print("arr2 after update", arr2)


