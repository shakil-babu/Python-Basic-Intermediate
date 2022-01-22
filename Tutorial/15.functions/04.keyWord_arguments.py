"""
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
"""

def func(a,b,c):
    print(c)


func(a = "shakil", c ="pagol", b = "pip")


"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of argum
"""


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")