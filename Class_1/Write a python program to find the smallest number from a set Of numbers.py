number = [2,3,5,74,2] 
# number.sort()

temp =0
for i in range(len(number)):
    for j in range(i+1, len(number)):
        if(number[i] > number[j]):
            temp = number[i]
            number[i] = number[j]
            number[j] = temp
print("The smallest number:",number[0])

 
        