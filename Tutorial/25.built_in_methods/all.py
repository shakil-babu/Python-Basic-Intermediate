"""
The all() function returns True if all elements in the given iterable are true. If not, it returns False.
"""

names = ["a","b","c"]
ans = all(names)
print(ans) # True


a = [0,1,1,2,2]
b = all(a)
print(b) # False


emty = []
res = all(emty)
print(res) # True