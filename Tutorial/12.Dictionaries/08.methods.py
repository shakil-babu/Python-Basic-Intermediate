details = {
    "name" : "Torikus sadik",
    "age" : 22,
    "favs": ["c","c++","js","python"]
}


# get method
name = details.get("name")
# print(name)

# copy method
copy = details.copy()
# print(copy)


# items method
items = copy.items()
# print(items)

# key method
keys = copy.keys()
print(keys)

# values method
values = copy.values()
print(values)


# pop method
poped = details.pop("age")
# print(poped)


# popItem
pop = details.popitem()
print(pop)