animal = open("animal.txt", "a+")
# r = read
# w = write
# r+ = read/ write
# w+ = read/ write truncate
# a+ = read / append
animal.seek(0)
text = animal.read()

print(text)

animal.write("elephant\n")

for i in range(0,5):
    user_input = input("enter a another names:")
    animal.write(user_input+"\n")
animal.close()

# with open("animal.txt","r") as file:
#     text = animal.read()
#     print(text)


# This creates a new file or overwrites if it already exists
# with open('example.txt', 'w') as file:
#     file.write("Hello, world!\n")
#     file.write("This is a second line.")
