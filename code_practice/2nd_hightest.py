num = [45,7,34,7,34,23,45,23,45,23,45,23,55,99]

new_num = num[0]

# new_num = max(num)
# for i in range(len(num)):
#     for j in range(i+1, len(num)):
#         if num[i] < num[j]:
#             new_num = num[j]
#             continue
# # sec_number  = new_num[1]
# # print("2nd hight number :",sec_number)
        
# print(new_num)

new_num = sorted(num)
print("the 2nd number :",new_num[len(new_num)-2])

