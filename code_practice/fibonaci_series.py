t1  = 0
t2 = 1

n = int(input("enter the number of terms: "))

next_t = t1 + t2

print("the series :", t1,t2,end=" ")
for i in range(3, n+1):
    print(next_t, end=" ")
    next_t = t1 + t2
    t1 = t2
    t2 = next_t
    next_t = t1 + t2

