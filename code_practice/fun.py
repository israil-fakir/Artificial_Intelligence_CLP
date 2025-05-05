
def max_find(new_list, m):
    for i in range(0, m):
        for j in  range(i+1, m):
            if new_list[i] < new_list[j]:
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp

    print("The sorted new list: ",new_list)
    print("Max value: ",new_list[0])


def find_max_if(new_list, m):
    max_val = new_list[0]
    for i in range(0, m):
        if i > max_val:
            max_val = i
    print("the max valuse using 'if' : ", max_val)


n = int(input("enter the size: "))
list2 = []
for i in range(n):
    ele = int(input("enter the elements :"))
    list2.append(ele)

print("the elements is :",list2)
max_find(list2, n)
find_max_if(list2, n)
list3 = sorted(list2,reverse=True)
print("the sorted list :",list3)
print("the max value useing sort_max", list3[0])


