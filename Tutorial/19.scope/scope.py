# local scope 
def sayNumber() :
    a = 10 # local variable
    print(a) # it's working

sayNumber()

# print(a) # it's not working

# global variable
c = 200
print(c)

def sayNum() :
    print(c)

sayNum()
