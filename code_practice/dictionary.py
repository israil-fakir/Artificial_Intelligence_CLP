new_dic = {
    "brand": "Ford",
    "model": "xyz",
    "year": 1990
}

print(new_dic)
print(type(new_dic))

cal =  {
    "brand": "casio",
    "model": "100ms",
    "year" : 2008
}

print(cal)

x = cal["year"]
print(x)

bd = new_dic["brand"]
print("the brand: ",bd)

cal["brand"] = "matrado"

print(cal)

cal["colour"] = "black"

print(cal)

cal.pop("colour")
print(cal)


for i in cal:
    print(i, end=" :--- ")
    print(cal[i])


new_cal = cal.copy()

print(new_cal)


print("level up")


nest_dic = {
    "childen": {
        "name": "A",
        "age": 35
    },
    "childen2":{
        "name": "b",
        "age": 45
    },
    "childen3": {
        "name": "C",
        "age": 6543
    }
}

print(nest_dic)