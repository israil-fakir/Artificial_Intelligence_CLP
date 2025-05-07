import numpy as ny


# arr = ny.array([3,5,7,4,7])
# print(arr)
# print(type(arr))


n = int(input("enter the size of array: "))
element = []
for i in range(0, n):
     ele = int(input("Enter the elements:"))
     element.append(ele)
print("the list", element)
print(type(element))
arr = ny.array(element)
print("the array:", arr)
print(type(arr))

print("level up: ")

print("enter the size of 2d arry:---")

new_element = []

row = int(input("enter the row number :"))
col = int(input("enter the col number :"))
for i in range(0, row):
    row_element= []
    for j in range(0, col):
        elements = int(input("enter {i} and {j} position:"))
        row_element.append(elements)
    new_element.append(row_element)
new_arr = ny.append(new_element)
print("the 2d array: ", new_arr)




