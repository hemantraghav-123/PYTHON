# person = {"name": "john" ,"age":"30","city":"london"}
# for value in person.values():
#     print(value)


# nested dictionaries
# dict = {
#     "name" : "Hemant",
#     "subjects" : {
#         "phy": 76,
#         "chem": 87,
#         "math": 99
#     }
# }
# print(dict)



# Dictionaries methods
# dict = {
#     "name" : "hemant",
#     "age" : 20,
#     "color" : "dusky",
#     "birth" : 2005,
#     "height" : 5.8
# }
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("color"))
# print(dict.update({"weight" : 55}))
# print(dict)


# store word meanings in dictionary
# dict= {
#     "table" : [" a piece of furniture", "list of figures and facts" ], "cat" : " a small animal"
# }
# print(dict)


# dict = {}
# x= int(input("enter marks of chem:"))
# dict.update({"chem": x})
# y= int(input("enter marks of physics:"))
# dict.update({"physics": y})
# z= int(input("enter marks of maths:"))
# dict.update({"maths": z})

# print(dict)


d = {1 : "pyhton" , 2 : [1, 2, 3]}
d.update({"one": 2})
print(d)