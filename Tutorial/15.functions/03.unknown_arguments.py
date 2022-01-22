"""
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""
def sayName (*names) :
    print("Hi " + names[1])


sayName('shakil','tori')



def sayFruit (*fruits):
    print ("First " + fruits[0])

sayFruit("apple","orange","pineapple")