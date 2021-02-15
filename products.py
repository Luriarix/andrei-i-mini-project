import csv
import os
from connection import connection, cursor


def clear():
    os.system( 'cls' )


prodChange = {}
# fieldheads = []
# prodList = []


def fieldNames():
    sql_test = "show fields from products"
    cursor.execute(sql_test)
    x = cursor.fetchall()
    return x


def productList():
    #
        # with open("products.csv", "r") as products:
        #     x = 0
        #     for item in products:
        #         print(f"{x} {item}".rstrip('\n').lstrip('0'))
        #         x += 1

        # with open("products.csv", "r") as products:
        #     prodList.clear()
        #     for item in csv.DictReader(products):
        #         prodList.append(item)

        # if fieldheads == []:
        #     with open("products.csv", "r") as products:
        #         for item in csv.DictReader(products).fieldnames:
        #             fieldheads.append(item)

    def allRows():
        sql = "SELECT * FROM products"
        cursor.execute(sql)
        y = cursor.fetchall()
        return y

    rowsValue = '' # stand in string for a row, so I can print it to the screen

    for i in allRows():
        z = 0 # I prefere the for(i) loop in C++, z stands in as a count
        for item in fieldNames():
            rowsValue += f'{item[0]}: {i[z]}     '
            z += 1
        print(rowsValue)
        rowsValue = ''


def addProduct():
    # for item in fieldheads:
    #     prodChange[item] = input('\nProduct {item}:\n')
    # prodChange = {
    #     'name':'mirinda',
    #     'price':'5.5'
    # }

    # with open("products.csv", "a", newline = '') as adding:
    #     writer = csv.DictWriter(adding, fieldheads)
    #     writer.writerow(prodChange)

    rowValues = "'Cola', 15"
    columnNames = ''
    z = 0 # standin for a count

    for item in fieldNames():
        print(item)
        print(item[1])
        if z == 1:
            columnNames += f"{item[0]}"
            # if 'char' in item[1]:
            #     rowValues += "'" + (input(f'\nProduct {item[0]}:\n')) + "'"
            # else:
            #     rowValues += (input(f'\nProduct {item[0]}:\n'))
        elif z != 0:
            columnNames += f", {item[0]}"
            # if 'char' in item[1]:
            #     rowValues += ", '" + (input(f'\nProduct {item[0]}:\n')) + "'"
            # else:
            #     rowValues += ", " + (input(f'\nProduct {item[0]}:\n'))
        z += 1

    sql = f"INSERT INTO products ({columnNames}) VALUES ({rowValues}); "
    # print(sql)
    cursor.execute(sql)
    connection.commit()
    # print(columnNames)


def print_to_screen_specific_prod(prod_id):
    sql = f"SELECT * FROM products WHERE id = {prod_id}"
    cursor.execute(sql)
    i = cursor.fetchone()
    print(f'1 id: {i[0]}    2 Name: {i[1]}    3 Price: {i[2]}\n')
    return i


def updateProduct():
    productList()

    newValue = ""
    newValueSet = ''
    columns = fieldNames()
    # field_names = []

    updateProd = int(input('\n0: Cancel\nSelect id of product to update:'))

    clear()
    prod = print_to_screen_specific_prod(updateProd)

    # try:
    #     prodList[updateProd - 1] == True
    # except IndexError:
    #     clear()
    #     print("\nThere is no such product! Try again!\n")
    #     updateProduct()

    # if updateProd != 0:
        # clear()
        # print(prodList[updateProd - 1])

        # x = 0
        # textVariable = '0: Cancel   '
        # for item in fieldheads:
        #     x += 1
        #     textVariable += f"{x}: {item}   "
        # print(f'\n{textVariable}')

        # detailToUpdate = int(input('\nWhich information to update: '))

        # if detailToUpdate != 0:
        #     print("\nCurrent Information: " + fieldheads[detailToUpdate - 1] + ': ' + prodList[updateProd - 1][fieldheads[detailToUpdate - 1]])
        #     prodList[updateProd - 1][fieldheads[detailToUpdate - 1]] = str(input(f'\nNew {fieldheads[detailToUpdate - 1]}:'))

    # writeProductList()

    whatToChange = int(input('1:All columns     2:One specific column\n'))

    if whatToChange == 1:
        z = 0 # standin for a count
        for item in columns:
            if z == 1:
                newValue = input(f'New {item[0]}:')
                if 'char' in item[1]:
                    newValueSet += f"{item[0]} = '{newValue}'"
                else:
                    newValueSet += f"{item[0]} = {newValue}"
            elif z != 0:
                newValue = input(f'New {item[0]}:')
                if 'char' in item[1]:
                    newValueSet += f", {item[0]} = '{newValue}'"
                else:
                    newValueSet += f", {item[0]} = {newValue}"
            z += 1

    elif whatToChange == 2:
        whichColumnToChange = int(input('Which column do you wanna change?  ')) - 1
        if 'char' in columns[whichColumnToChange][1]:
            newValue = input(f'New {columns[whichColumnToChange][0]}:  ')
            newValueSet = f"{columns[whichColumnToChange][0]} = '{newValue}'"
        else:
            newValue = int(input(f'New {columns[whichColumnToChange][0]}:  '))
            newValueSet = f"{columns[whichColumnToChange][0]} = '{newValue}'"

    sql = f"UPDATE products SET {newValueSet} WHERE id = {updateProd};"
    # print(sql)
    cursor.execute(sql)
    connection.commit()


def deleteProduct():
    productList()
    prodDel = int(input('\nId of product to delete: '))

    # prodList.pop(prodDel - 1)
    # writeProductList()

    sql = f"DELETE from products where id =  {prodDel}"
    cursor.execute(sql)
    connection.commit()


# def writeProductList():
#     with open("products.csv", "w", newline = '') as change:
#         writer = csv.DictWriter(change, fieldheads)
#         writer.writeheader()
#         writer.writerows(prodList)

