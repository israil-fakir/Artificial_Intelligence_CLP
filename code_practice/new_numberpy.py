import numpy as ny

arr1 = ny.array([4,5,3,4])
arr2 = ny.array([46,23,56,34])
arr = ny.concatenate((arr1,arr2))
print(arr)

new_arr = ny.sort(arr)
print(new_arr)
