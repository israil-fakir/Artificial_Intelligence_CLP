

num = int(input("enter the number to find the factorail: "))

mul = 1

for i in range(1, num+1):
    mul = mul * i
print("the fact : ", mul)

print("using the while loop")

n = int(input("enter the number: "))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1
print("the fact : ", fact)