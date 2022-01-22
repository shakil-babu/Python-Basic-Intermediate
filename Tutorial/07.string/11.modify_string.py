# string modifies

name = " Shakil babu "

# upper
print(name.upper()) # output : SHAKIL BABU

# lower
print(name.lower()) # output: shakil babu

# strip() -> remove white space from left and right
print(name.strip()) # output:shakil babu
print(name.lstrip()) # output:shakil babu 
print(name.rstrip()) # outptu: shakil babu


# replace
print(name.replace("Shakil", "Rahim"))
# output : Rahim babu


# split string
bio = "I am babu"
arr = bio.split(" ")
print(arr)