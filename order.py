import csv
import os

def clear():
    os.system( 'cls' )

orderChange = {}
fieldheads = []
ordList = []
productList = []
courierList = []
test = []

statuses = ['preparing', 'delivering', 'done']


def orderList():
    with open("test.csv", "r") as orders:
        x = 0
        for item in orders:
            print(f"{x} {item}".rstrip('\n').lstrip('0'))
            x += 1

    with open("test.csv", "r") as orders:
        ordList.clear()
        for item in csv.DictReader(orders):
            ordList.append(item)

    if fieldheads == []:
        with open("test.csv", "r") as orders:
            for item in csv.DictReader(orders).fieldnames:
                fieldheads.append(item)



def addOrder():
    # for item in fieldheads:
    #     if item != 'status':
    #         order = input(f"Add {item}: ")
    #         orderChange[item] = str(order)
        # elif item == 'courier':
            # courierList()
    #         print("Please select a courier?/
    #             Please input the couriers id:")
    #         order = input(f"Add {item}: ")
    #         orderChange[item] = str(order)
    #     elif item == 'order':
            # productList()
    #         print("What would you like to order?\
        # (Input 0 to confirm selection)/
    #             Please input the products id:")
    #         while order != "0":
    #             order = input()
    #             productList.append(order)
    #         orderChange[item] = str(order)
    #     else: orderChange[item] = 'preparing'
    #     clear()
    # for item in fieldheads:
        # print(orderChange[item])

    orderChange = {
        'name': 'mike',
        'address': 'stars',
        'phone': '00000',
        'courier': 'Bobbie',
        'order': 'burger',
        'status': 'preparing'
    }

    with open("test.csv", "a", newline = '') as adding:
        writer = csv.DictWriter(adding, fieldheads)
        writer.writerow(orderChange)


def updateOrder():
    updateOrd = input('\n0: Cancel   1: Update a Order   2: Update a Orders Status\n')
    if updateOrd == '1':
        orderList()
        selectedOrder = int(input('\nWhich order number to update: ')) - 1
        clear()

        x = 0
        textVariable = ''
        for item in fieldheads:
            x += 1
            if item == 'status':
                break
            textVariable += f"{x}: {item}   "
        print(f'\n{textVariable}')

        detailToUpdate = int(input('\nWhich information to update: ')) - 1

        print("\nCurrent Information: " + fieldheads[detailToUpdate] + ': ' + ordList[selectedOrder][fieldheads[detailToUpdate]])

        newDetails = str(input('\nNew Information: '))
        ordList[selectedOrder][fieldheads[detailToUpdate]] = newDetails

        clear()
        print('\nUpdated Order List:\n')

    elif updateOrd == '2':
        orderList()
        selectedOrder = int(input('\nOrder status to change: ')) - 1

        print('Statuses available:')
        x = 0
        textVariable = ''
        for item in statuses:
            x += 1
            textVariable += f'{x}: {item}   '
        print(f'\n{textVariable}')
        newStatus = int(input('\nNew Status entry: '))
        ordList[selectedOrder]['status'] = statuses[newStatus]

        clear()
        print('\nUpdated Order List:\n')

    elif updateOrd == '0':
        clear()
        print('\nCurrent Orders:\n')

    else:
        clear()
        print("\nDon't know whatcha talking about! Try again!\n")
        updateOrder()

    with open("test.csv", "w", newline = '') as change:
        writer = csv.DictWriter(change, fieldheads)
        writer.writeheader()
        for item in ordList:
            writer.writerow(item)


def deleteOrder():
    orderList()
    x = len(ordList)
    print('\nSelect 0 to cancel.')
    orderDel = int(input('\nNumber of order to delete: '))

    if orderDel == 0:
        clear()
        print('\nCurrent Orders:\n')

    elif 0 < orderDel <= len(ordList):
        with open("test.csv", "w", newline = '') as change:
            writer = csv.DictWriter(change, fieldheads)
            writer.writeheader()
            for item in ordList:
                if ordList.index(item) != orderDel - 1:
                    writer.writerow(item)
        clear()
        print('\nNew Order List:\n')

    else:
        clear()
        print("\nDon't know whatcha talking about! Try again!\n")
        deleteOrder()

