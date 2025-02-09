import numpy as np

arr = np.random.randint(1,10,(5,5))
# print(arr)
print("Generate the 5*5 matrix:")
for i in arr:
    print(i)

row_sum = np.sum(arr,axis=1)
print("Row wise sum:")
for i in row_sum:
    print(i)