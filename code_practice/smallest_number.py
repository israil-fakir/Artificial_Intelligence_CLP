num = [42,5,2,7,5,3,7]

# print("the smallest number :", min(num))
# without built in function

smallest = num[0]
for i in range(len(num)):
    if num[i] < smallest:
        smallest = num[i]
    else:
        continue

print("the smallest number is :", smallest)
