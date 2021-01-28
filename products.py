# arsalan was here
def productList():
    # products = open("test.txt", "r") #['Coke', 'Sprite']

    with open("test.txt", "r") as products:
        item = products.read()
        print(item)
    # for item in products:
    #     print(f"{item}".rstrip())

    # products.close()


def addProduct():
    # adding = open("test.txt", "a")
    with open("test.txt", "a") as adding:
        adding.write(input('\nName of new products:\n').lower()+"\n")
    # adding.close()


def updateProduct():
    # products = open("test.txt", "r")
    prodList = []

    prodChange = input('\nProduct to change:\n')
    newProd = input('\nNew product:\n')

    with open("test.txt", "r") as products:
        for item in products:
            prodList.append(f"{item}".rstrip())

    try:
        prodList.index(prodChange)
    except ValueError:
        print("There is no such product!\n")

    # products.close()
    # change = open("test.txt", "w")

    with open("test.txt", "w") as change:
        for item in prodList:
            if item == prodChange:
                change.write(newProd + "\n")
            else:
                change.write(item + "\n")

    # change.close()


def deleteProduct():
    # products = open("test.txt", "r")
    prodList = []

    prodDel = input('\nProduct to delete:\n')

    with open("test.txt", "r") as products:
        for item in products:
            if item != prodDel + "\n":
                prodList.append(item)

    # products.close()
    # change = open("test.txt", "w")

    with open("test.txt", "w") as change:
        for item in prodList:
            change.write(item)

    # change.close()