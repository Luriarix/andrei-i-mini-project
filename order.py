import csv
import os
from connection import connection, cursor
from couriers import courierList
from products import productList


def clear():
    os.system( 'cls' )


def fieldNames(): # thought it might be easier for me to get the column details
    sql_order = [
        'show fields from orders',
        'show fields from products',
        'show fields from courier'
        ]
    x = tuple()
    for i in sql_order:
        x += connection.execute(i)
    return x


def orderList():#, p.name AS Products, p.price as Price
    def allRows():
        sql = "SELECT o.*, p.*, c.*\
        FROM orders o\
        left JOIN courier c on c.id = o.courier_id\
        left JoIN productToOrder po ON o.id = po.order_id\
        left JOIN products p on p.id = po.product_id"
        return connection.execute(sql)

    rowsValue = '' # stand in string for a row, so I can print it to the screen

    for i in allRows():
        z = 0 # I prefere the for(i) loop in C++, z stands in as a count
        for item in fieldNames():
            if 'id' in item[0] and z != 0:
                z += 1
            if z == 0 or 'id' not in item[0]:
                rowsValue += f'{item[0]}: {i[z]}     '
                if z == len(i):
                    break
                z += 1
        print(rowsValue)
        rowsValue = ''


def addOrder():# I commented where it asks for the user input, for speeds sake
    rowValues = "'mike', 'stars', 00000, 'preparing', 2"# once I uncomment the user input I'l make this an empty string
    columnNames = ''
    z = 0

    for item in fieldNames():
        if 'id' in item[0] and z != 0:# making sure to add a courier id and breaking before an error pops up
            # while True:
                # courierList()
                # selectedCourier = int(input('Please select a couriers ID: '))
                # try:
                #     sql = f"SELECT id\
                #     FROM courier\
                #     WHERE id = {selectedCourier}"
                #     connection.execute(sql)
                #     break
                # except:
                #     print("Please select something that is available. (This choice is mandatory.)")
            columnNames += f"{item[0]} ,"
            break

        elif z != 0:
            # temp = (input(f'\nProduct {item[0]}:\n'))
            # if temp != '':
                columnNames += f"{item[0]} ,"
                # if 'char' in item[1]:
                #     if 'status' in item[0]:
                #         rowValues += "'preparing', "
                #     else:
                #         rowValues += f"'{temp}', "
                # else:
                #     rowValues += f"{temp}, "
        z += 1
    # rowValues += selectedCourier

    sql = f"INSERT INTO orders ({columnNames.rstrip(',')}) VALUES ({rowValues}); " # creates a new order
    connection.execute(sql)

    sql = "SELECT id FROM orders ORDER BY id desc"# gets me the id of the last order created (hopefully)
    latestRow = connection.execute(sql)
    print(latestRow[0][0])

    clear()
    while True:# to make sure I can add as many prod as I want
        productList()
        prodToAdd = int(input('0:To stop adding crap  \nPick a product ID:'))

        if prodToAdd == 0:
            break

        sql = f"INSERT INTO productToOrder VALUES ({latestRow[0]}, {prodToAdd})"

        try:
            connection.execute(sql)
        except:
            clear()
            print("Yeah... the product selected doesn't exist, pick one I can actually give you, please.")


def updateOrder(): # I put update status and a specific value here
    updateOrd = input('\n0: Cancel   1: Update a Order   2: Update a Orders Status\n')
    if updateOrd == '1':# still working on this one 
        rowsValue = ''

        orderList()# wanted to print the current order list before selecting something
        selectedOrder = int(input('\nWhich order Id to update: '))
        clear()

        sql = f"SELECT *\
        FROM orders\
        WHERE o.id = {selectedOrder}"
        cursor.execute(sql)
        x = cursor.fetchall()

        for i in x:
            z = 0 # I prefere the for(i) loop in C++, z stands in as a count
            for item in fieldNames():
                rowsValue += f'{z}: {item[0]}: {i[z]}     '
                if z == len(i):
                    break
                z += 1
            print(rowsValue)
            rowsValue = ''

        detailToUpdate = int(input('\nWhich information to update: '))

        # print("\nCurrent Information: " + fieldheads[detailToUpdate] + ': ' + ordList[selectedOrder][fieldheads[detailToUpdate]])

        newDetails = str(input('\nNew Information: '))
        # ordList[selectedOrder][fieldheads[detailToUpdate]] = newDetails

        clear()
        print('\nUpdated Order List:\n')

    elif updateOrd == '2': # Updates order status, works for now
        rowsValue = '' # stand in string for a row, so I can print it to the screen
        statuses = ['delivering', 'done']
        orderList()# wanted to print the current order list before selecting something
        selectedOrder = int(input('\nOrder status to change: '))

        sql = f"SELECT *\
        FROM orders\
        WHERE id = {selectedOrder}"
        orderToUpdate = connection.execute(sql)

        z = 0 # I prefere the for(i) loop in C++, z stands in as a count
        for item in fieldNames(): # prints it nicely
            if z == 0 or 'id' not in item[0]:
                rowsValue += f'{item[0]}: {orderToUpdate[0][z]}     '
                z += 1
            else:
                break

        while True:# this is here more for error caching
            print(rowsValue)

            print('Statuses available:')
            x = 0 # standin as counter
            textVariable = ''
            for item in statuses: # same as previous for loop but for the list of statuses
                x += 1
                textVariable += f'{x}: {item}   '
            print(f'\n{textVariable}')

            newStatus = int(input("\nPick a new status by number: ")) - 1
            sql = f"UPDATE orders SET order_status = '{statuses[newStatus]}' WHERE id = {orderToUpdate[0]}"

            try:
                connection.execute(sql)
                break
            except:
                clear()
                print("Yeah... the order or status selected doesn't exist, pick one I can actually use, please.")

        clear()
        print('\nUpdated Order List:\n')

    elif updateOrd == '0':
        clear()
        print('\nCurrent Orders:\n')

    # else:
    #     clear()
    #     print("\nDon't know whatcha talking about! Try again!\n")
    #     updateOrder()


def deleteOrder():# works and it should work properly
    orderList()# wanted to print the current order list before selecting something
    orderDel = int(input('\nSelect 0 to cancel. \nNumber of order to delete: '))

    if orderDel == 0:
        clear()
        print('\nCurrent Orders:\n')

    else:
        sql = f"DELETE FROM orders\
        WHERE id = {orderDel}"

        try:
            connection.execute(sql)
        except:
            clear()
            print("Yeah... the order selected doesn't exist, pick one I can actually delete, please.")
            deleteOrder()

        clear()
        print('\nNew Order List:\n')