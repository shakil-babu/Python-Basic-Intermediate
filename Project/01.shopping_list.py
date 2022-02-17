# ===================== simple shopping list app ============================
# list
shopping_list = []

# showHelp function


def showHelp():
    print("Enter <Done> for terminate!")
    print("Enter <Show> for see shopping list!")
    print("Enter <lastItem> for last shopping item!")
    print("Enter <firstItem> for first shopping item!")


# shoppingList
def shoppingList():
    print(shopping_list)


# lastItem function
def lastItem():
    print(shopping_list[-1])


# firstItem function
def firstItem():
    print(shopping_list[0])


print("Enter <Done> for exit!")
print("Enter <Help> for more informations!")
while True:
    item = input("> ")
    if item == "Done":
        break
    elif item == "Help":
        showHelp()
    elif item == "Show":
        shoppingList()
    elif item == "lastItem":
        lastItem()
    elif item == "firstItem":
        firstItem()
    else:
        shopping_list.append(item)
