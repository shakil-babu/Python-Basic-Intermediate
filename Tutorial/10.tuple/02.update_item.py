
# tuple
details = ("shakil",21,"torikus",22,'sadik',23)

"""
tuple is unchangeable in that case we can convert tuple into list 

"""


# convert into list
dt = list(details)

dt.append("babu")
dt[0] = "shakilbabu"
del dt[1]


# convert into tuple
x = tuple(dt)

print(x)