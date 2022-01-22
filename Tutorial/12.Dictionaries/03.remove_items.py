
# dictionaries declaration
details = {
    "name" : "shakil",
    "age" : 21,
    "Dream" : "Software Engineer",
    "Favlans" : ["JavaScript","TypeScript","C++","Python"]
}

# pop() method removes the item with specified key name
details.pop("Favlans")
print(details)


# pop item method removes the last item
details.popitem()
print(details)


"""
Also we can perm these methods:
-> clear()
-> del
"""