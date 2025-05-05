x = [54,23,5,7,9,23,78,24,8]
# print(x[2])

sum_even = 0
sum_odd =0 
for i in range(len(x)):
    if x[i] % 2 == 0:
        sum_even = sum_even + x[i]
    else:
        sum_odd = sum_odd + x[i]

print( "Sum of even numbers is :", sum_even)
print("Sum of odd numbers is :", sum_odd)