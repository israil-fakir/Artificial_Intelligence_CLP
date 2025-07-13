number = [1, 2, 3, 4, 5, 6, 7, 8]

even_sum = 0
odd_sum = 0
for i in number:
    if(i % 2 == 0):
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print("Even Sum",even_sum)
print("Odd sum",odd_sum)