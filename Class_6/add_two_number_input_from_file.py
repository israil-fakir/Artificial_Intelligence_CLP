# a = int(input("enter a number :"))
# b = int(input("enter another number :"))

input_number = open("add_two_number_file.txt","r+")

numbers_from_fils = input_number.readlines()
a = int(numbers_from_fils[0].strip())
b = int(numbers_from_fils[1].strip())

c = a+b
print("The result: ", c)