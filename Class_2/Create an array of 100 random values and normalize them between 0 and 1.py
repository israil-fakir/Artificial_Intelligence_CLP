import numpy as np

arr = np.random.randint(1, 10, 100)

print("Random array elements :", arr)

min_rang = 0
max_rang = 1

normalize = ( (arr - np.min(arr)) / (np.max(arr) - np.min(arr)) ) * (max_rang-min_rang) + min_rang
print()
print("The normalizations values :",normalize)
