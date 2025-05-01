x = 50
y = 55.5
print(x)
print(type(x))

print(y)
print(type(y))

nam = "Ahemed"
print(nam)
print(type(nam))

new_x = str(34)

print(new_x)
print(type(new_x))


# st = int("string")
# print(st)
# print(type(st)) not working

x, y, z = 1, 2, 3
print(x, y, z) # varable and valuse must be same

x = y =z = 99
print(x)
print(y)
print(z)

fruits = ["mango", "apple","cherry"]
p, q, r = fruits
print(p, q, r)


print(p+q+r)


num = 10
st_nam = " Opi "
# print(num + st_nam) #not working

print(str(num) + st_nam)

# Global variable

val = 44

def my_fun():
    print(val)
    
my_fun()


def fun():
    my_weight = 64
    
# print(my_weight) the my_weight is not found in globaly

def new_fun():

    global score 
    score = 46
    print("Print from function", score)
new_fun()
print("print from outside the function", score)

