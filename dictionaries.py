my_info = {
    "name" : "Meet",
    "age" : 21,
    "city" : "Agra",
    "score" : 80.0
}
print(my_info)
print(type(my_info))
print(my_info["city"])
print(my_info["score"])
print(my_info["age"])
print(my_info["name"])
print(my_info.get("school","st george's"))

del my_info["score"]
print(my_info)

