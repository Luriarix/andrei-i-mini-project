import csv
import os


def clear():
    os.system( 'cls' )


prodChange = {}
fieldheads = []
prodList = []


def productList():
    with open("products.csv", "r") as products:
        x = 0
        for item in products:
            print(f"{x} {item}".rstrip('\n').lstrip('0'))
            x += 1

    with open("products.csv", "r") as products:
        prodList.clear()
        for item in csv.DictReader(products):
            prodList.append(item)

    if fieldheads == []:
        with open("products.csv", "r") as products:
            for item in csv.DictReader(products).fieldnames:
                fieldheads.append(item)


def addProduct():
    # for item in fieldheads:
    #     prodChange[item] = input('\nProduct {item}:\n')
    prodChange = {
        'name':'mirinda',
        'price':'5.5'
    }

    with open("products.csv", "a", newline = '') as adding:
        writer = csv.DictWriter(adding, fieldheads)
        writer.writerow(prodChange)


def updateProduct():
    productList()
    updateProd = int(input('\n0: Cancel\nSelect product to update:'))

    try:
        prodList[updateProd - 1] == True
    except IndexError:
        print("There is no such product!\n")
        updateProduct()

    if updateProd != 0:
        clear()
        print(prodList[updateProd - 1])

        x = 0
        textVariable = '0: Cancel   '
        for item in fieldheads:
            x += 1
            textVariable += f"{x}: {item}   "
        print(f'\n{textVariable}')

        detailToUpdate = int(input('\nWhich information to update: '))

        if detailToUpdate != 0:
            print("\nCurrent Information: " + fieldheads[detailToUpdate - 1] + ': ' + prodList[updateProd - 1][fieldheads[detailToUpdate - 1]])
            prodList[updateProd - 1][fieldheads[detailToUpdate - 1]] = str(input(f'\nNew {fieldheads[detailToUpdate - 1]}:'))

    writeProductList()


def deleteProduct():
    productList()
    prodDel = int(input('\nProduct entry to delete:'))

    prodList.pop(prodDel - 1)

    writeProductList()


def writeProductList():
    with open("products.csv", "w", newline = '') as change:
        writer = csv.DictWriter(change, fieldheads)
        writer.writeheader()
        writer.writerows(prodList)
