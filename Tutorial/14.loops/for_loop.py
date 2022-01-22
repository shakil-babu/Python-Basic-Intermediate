# for loop 

# looping through in list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



# loop in string
for x in "banana":
  print(x)


# break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break



# continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# range function
for x in range(6):
  print(x)



# use the starter number
for x in range(2, 6):
  print(x)


"""
The range() function defaults to increment the sequence by 1, 
however it is possible to specify the increment value 
by adding a third parameter: range(2, 30, 3):
"""

for x in range(2, 30, 3):
  print(x)


# loop with else keyword
for x in range(6):
  print(x)
else:
  print("Finally finished!")