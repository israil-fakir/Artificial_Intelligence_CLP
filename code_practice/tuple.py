from code_practice.data_type_list import fruits

new_tuple = ("hi", "hello", "good",3,5)
print(new_tuple)
print(type(new_tuple))
print(len(new_tuple))

new_str = ("str")
print(type(new_str))


tuple2= (("a", "b", "c","d","e", "f","g"))
print(tuple2)
print(type(tuple2))
for i in tuple2:
    print(i)
print("tuple index[1]: ", tuple2[1])
print("the range [:3] ", tuple2[:3])
# print("pop a item:", tuple2.remove())
new_list = list(tuple2)
new_list[0] = "A"
tuple2 = tuple(new_list)
print("after assign 'A' valuse ", tuple2)



