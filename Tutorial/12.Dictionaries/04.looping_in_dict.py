
# dictionaries declaration
details = {
    "name" : "shakil",
    "age" : 21,
    "Dream" : "Software Engineer",
    "Favlans" : ["JavaScript","TypeScript","C++","Python"]
}

# loop through using key
for key in details:
    print(key)


# print values
for key in details:
    print(details[key])


# only values
for value in details.values():
    print(value)


# only keys
for key in details.keys():
    print(key)

# items
for key,value in details.items():
    print(key,value)