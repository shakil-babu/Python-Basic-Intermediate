
# dictionaries declaration
details = {
    "name" : "shakil",
    "age" : 21,
    "Dream" : "Software Engineer",
    "Favlans" : ["JavaScript","TypeScript","C++","Python"]
}


# access items
name = details["name"]
print(name)

# using get method
dream = details.get("Dream")
print(dream)


# get keys
keys = details.keys()
print(keys)

# get values
values = details.values()
print(values)


items = details.items()
ans = []
for item in items:
    arr = list(item)
    for ele in arr:
        if ele == "name":
            ans.append(item)


print(ans)
