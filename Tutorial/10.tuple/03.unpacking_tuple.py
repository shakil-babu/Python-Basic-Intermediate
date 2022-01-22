
# tuple
from os import name


fruits = ("Apple", "Banana", "Orange", "Mango")

(apple, banana, *all) = fruits

print(apple)
print(banana)
print(all)
