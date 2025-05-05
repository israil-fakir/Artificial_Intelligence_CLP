
def find_max(num):
    list2 = []
    for i in range(0, num):
        num = int(input("enter the list value:"))
        list2.append(num)

    for i in range(0, num):
        for j in range(i+1, num):
            if list2[i] < list2[j]:
                tm = list2[i]
                list2[i] = list2[j]
                list2[j] = tm

    print(list2)

    print("the max value:", list2[0])







def max_find_without_sorting:


n = int(input("enter the list size: "))
find_max(n)
max_find_without_sorting(n)










