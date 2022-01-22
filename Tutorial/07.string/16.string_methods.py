# string methods

# ============== find/index method =============
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
print(txt.index('welcome'))



# =============== rindex/rfind ============
txt = "say hello from mind"
x = txt.rindex(" ")
print(x)
print(txt.rfind('mind'))



# =================== Join method ===============
names = ['shakil','fahim','torikus']
afterJoined = "+".join(names)
print(afterJoined)


# with tuple
dreams = ("programmer","engineer","developer")
afterJoinedAges = "-".join(dreams)
print(afterJoinedAges)


# with object
myDict = {"name": "John", "country": "Norway"}
mySeparator = "--"

x = mySeparator.join(myDict)
print(x)


# ============== isalpha
txt = "Company10"
x = txt.isalpha()
print(x)


# startswith
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# translate method
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
