num = int(input("Enter the Fibonacci sequence : "))

t0 = 0
t1 = 1
next_t = t0+t1
print("The Series: ",t0,t1,end=" ")
for i in range(3, num+1):
    print(next_t, end=" ")
    t0 = t1
    t1 = next_t
    next_t = t0+t1
  