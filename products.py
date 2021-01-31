prodList = []

def productList():
    with open("products.txt", "r") as products:
        for item in products:
            prodList.append(item.rstrip())
            print(f"{item}".rstrip().capitalize())


def addProduct():
    with open("products.txt", "a") as adding:
        adding.write(input('\nName of new products:\n').lower()+"\n")


def updateProduct():
    prodChange = input('\nProduct to change:\n').lower()

    try:
        prodList.index(prodChange)
    except ValueError:
        print("There is no such product!\n")

    newProd = input('\nNew product:\n').lower()

    with open("products.txt", "w") as change:
        for item in prodList:
            if item == prodChange:
                change.write(newProd + "\n")
            else:
                change.write(item + "\n")

    prodList.clear()


def deleteProduct():
    prodList.clear()
    prodDel = input('\nProduct to delete:\n').lower()

    with open("products.txt", "r") as products:
        for item in products:
            if item != prodDel + "\n":
                prodList.append(item)

    with open("products.txt", "w") as change:
        for item in prodList:
            change.write(item)

    prodList.clear()