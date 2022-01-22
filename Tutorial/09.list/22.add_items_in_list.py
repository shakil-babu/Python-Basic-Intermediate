# add list items
li = [10,20,30,40]
# append - added an itme in the last
li.append(100)
print(li)

# insert - added item using index
li.insert(0,100)
print(li)


# extend
li1 = ['sha','kil','babu']
li.extend(li1)
print(li)


""" 
The extend() method does not have to append lists, 
you can add any iterable object (tuples, sets, dictionaries etc.).
"""
a = [1,2]
b = (3,4)
a.extend(b)
print(a)