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
        cursor.execute(i)
        x += cursor.fetchall()
    return x


def orderList():#, p.name AS Products, p.price as Price
    def allRows():
        sql = "SELECT o.*, p.*, c.*\
        FROM orders o\
        left JOIN courier c on c.id = o.courier_id\
        left JoIN productToOrder po ON o.id = po.order_id\
        left JOIN products p on p.id = po.product_id"

        cursor.execute(sql)
        y = cursor.fetchall()
        return y

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
            columnNames += f"{item[0]} ,"
            courierList()
            # selectedCourier = int(input('Please select a couriers ID: '))
            break
        elif z != 0:
            columnNames += f"{item[0]} ,"
            # if 'char' in item[1]:
            #     if 'status' in item[0]:
            #         rowValues += "'preparing', "
            #     else:
            #         rowValues += "'" + (input(f'\nProduct {item[0]}:\n')) + "', "
            # else:
            #     rowValues += (input(f'\nProduct {item[0]}:\n')) + ", "
        z += 1
    # rowValues += selectedCourier

    sql = f"INSERT INTO orders ({columnNames.rstrip(',')}) VALUES ({rowValues}); " # creates a new order
    cursor.execute(sql)
    connection.commit()

    sql = "SELECT id FROM orders ORDER BY id desc"# gets me the id of the last order created (hopefully)
    cursor.execute(sql)
    latestRow = cursor.fetchone()
    print(latestRow[0])

    clear()
    while True:# to make sure I can add as many prod as I want
        productList()
        prodToAdd = int(input('0:To stop adding crap  \nPick a product ID:'))

        if prodToAdd == 0:
            break

        sql = f"INSERT INTO productToOrder VALUES ({latestRow[0]}, {prodToAdd})"

        try:
            cursor.execute(sql)
        except:
            clear()
            print("Yeah... the product selected doesn't exist, pick one I can actually give you, please.")

        connection.commit()


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
        statuses = ['delivering', 'done']

        orderList()# wanted to print the current order list before selecting something
        selectedOrder = int(input('\nOrder status to change: '))

        sql = f"SELECT *\
        FROM orders\
        WHERE id = {selectedOrder}"
        cursor.execute(sql)
        orderToUpdate = cursor.fetchone()

        rowsValue = '' # stand in string for a row, so I can print it to the screen

        z = 0 # I prefere the for(i) loop in C++, z stands in as a count
        for item in fieldNames(): # prints it nicely
            if z == 0 or 'id' not in item[0]:
                rowsValue += f'{item[0]}: {orderToUpdate[z]}     '
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
                cursor.execute(sql)
                break
            except:
                clear()
                print("Yeah... the order or status selected doesn't exist, pick one I can actually use, please.")

            connection.commit()

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
    print('\nSelect 0 to cancel.')
    orderDel = int(input('\nNumber of order to delete: '))

    if orderDel == 0:
        clear()
        print('\nCurrent Orders:\n')

    else:
        sql = f"DELETE FROM orders\
        WHERE id = {orderDel}"

        try:
            cursor.execute(sql)
        except:
            clear()
            print("Yeah... the order selected doesn't exist, pick one I can actually delete, please.")
            deleteOrder()

        connection.commit()

        clear()
        print('\nNew Order List:\n')