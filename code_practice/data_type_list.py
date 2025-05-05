

fruits = (("apple", "banana", "orange")) # tuple
print(fruits)
print(type(fruits))


fruits = ["apple", "banana", "orange"] # list
print(fruits)
print(type(fruits))

new_fruits = list(("Napple", "Nbanana", "Norange")) # list
print(new_fruits)
print(type(new_fruits))

fruits = {"apple", "banana", "orange"} # set
print(fruits)
print(type(fruits))
# print(fruits[0]) # set does not support indexing


 
fi = "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0"
 
flag = 0
count = 0
print("len: ", len(fi))
for i in range(len(fi)):
    if fi[i] == "1":
        flag = flag + 1        
    elif fi[i] == "0":
        count = count + 1
    else:
        print("invalid input")
print("flag: ", flag)
print("count: ", count)


print("level 1")

water = ["sea","river","lake"]
print("index -o:", water[0]) 

print("index range 0 to 2:", water[0:len(water)])

water.append("ocean")
print("after appending :",water) #add in last index


water.insert(0, "pond")
print("after insert at '0' index: ", water) #add in first index
for i in range(len(water)):
    print(water[i], end="    ")

new_water = water.copy()

print("\n")

water.remove("sea")
print("after just used the remove function :", water) #remove the first index

water.pop(0)
print("after just used the pop function :", water) #remove the index from first

water.pop(1)
print(water) #also work with index 


print("\nlevel 2")
for i in water:
    print(i)
print("level 2 end")

list1 = [1,2,3,4,5] 
list2 = [6,7,8,9,10]

list3 = list1 + list2
print("list3: ", list3)
print(type(list3))
list3.clear()
print("list3 after clear: ", list3)

count_6 = list2.count(6)
print(count_6)


print("level 3")
print("sum from a list:")
list4 = [2,4,6,8,10]
sum = 0
for i in range(len(list4)):
    sum = sum + list4[i]

print("sum of list4: ", sum)
    
print("same work")

list5 = []

new_sum = 0
n = int(input("enter the element number "))
for i in range(0, n):
    element = int(input("enter the element to sum them:"))
    list5.append(element)
    new_sum = new_sum + list5[i]
print("the list5 is :", list5)
print("sum of list5: ", new_sum)
