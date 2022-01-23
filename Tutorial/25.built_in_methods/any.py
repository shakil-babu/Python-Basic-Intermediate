"""
The any() function returns True if any element of an iterable is True. If not, 
it returns False.
"""

nums = [10,20,30,0]
ans = any(nums)
print(ans) # True


n = [0,0,0,0]
res = any(n)
print(res) # False


# if list/tuple/set/dic is emty then return False
a = []
b = any(a)
print(b)