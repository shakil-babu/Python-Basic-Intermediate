# remove items from list
li = [1,3,4,5]

# remove - delete using value
li.remove(1) 
print(li)

# pop - delete specific item using index otherwise last item
li.pop(1)  # delete 1 no value
print(li)
li.pop() # delete last value


# using del method
listt = [10,20,30]
del listt[0]

# clear
listt.clear()
