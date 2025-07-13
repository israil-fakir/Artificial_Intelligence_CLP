def larger_finder(x,y):
    if(x>y):
        print("The largest number :",x)
    else:
        print("The largest number :",y)


print("Enter the two number to find largest number")

a = int(input("1st number :"))
b = int(input("2nd number :"))
larger_finder(a,b)