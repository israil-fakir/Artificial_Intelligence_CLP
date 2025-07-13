s = 50
f = 100

print("The Summation: ", end="")
total_sum = 0
for i in range(s, f + 1):
    if i % 3 == 0 and i % 5 != 0:        
        total_sum = total_sum + i
        #print("series:",i,end=" ")
        
print(total_sum)