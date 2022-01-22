
# a = {10,20,30,40}
# b = {100,200}

# c = a.union(b)
# print(c)


# x = {10,20}
# y = {40,30}
# x.update(y)
# print(x)



# print common items from 2 sets without new set
xx = {10,20,30,40,50}
yy = {10,20,88}

xx.intersection_update(yy)
print(xx)


# contains common items from 2 sets with new set
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)


# uncommon items from 2 sets with new set
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)