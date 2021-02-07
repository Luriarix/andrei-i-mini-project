import csv
import os


def clear():
    os.system( 'cls' )


courChange = {}
fieldheads = []
courList = []


def courierList():
    with open("couriers.csv", "r") as couriers:
        x = 0
        for item in couriers:
            print(f"{x} {item}".rstrip('\n').lstrip('0'))
            x += 1

    with open("couriers.csv", "r") as couriers:
        courList.clear()
        for item in csv.DictReader(couriers):
            courList.append(item)

    if fieldheads == []:
        with open("couriers.csv", "r") as couriers:
            for item in csv.DictReader(couriers).fieldnames:
                fieldheads.append(item)


def addCourier():
    # for item in fieldheads:
    #     courChange[item] = input('\nCourier {item}:\n')
    courChange = {
        'name':'mark',
        'phone':'666'
    }

    with open("couriers.csv", "a") as adding:
        writer = csv.DictWriter(adding, fieldheads)
        writer.writerow(courChange)


def updateCourier():
    courierList()
    updateCour = int(input('\n0: Cancel\nSelect courier to update:'))

    try:
        courList[updateCour - 1] == True
    except IndexError:
        print("There is no such product!\n")
        updateCourier()

    if updateCour != 0:
        clear()
        print(courList[updateCour - 1])

        x = 0
        textVariable = '0: Cancel   '
        for item in fieldheads:
            x += 1
            textVariable += f"{x}: {item}   "
        print(f'\n{textVariable}')

        detailToUpdate = int(input('\nWhich information to update: '))

        if detailToUpdate != 0:
            print("\nCurrent Information: " + fieldheads[detailToUpdate - 1] + ': ' + courList[updateCour - 1][fieldheads[detailToUpdate - 1]])
            courList[updateCour - 1][fieldheads[detailToUpdate - 1]] = str(input(f'\nNew {fieldheads[detailToUpdate - 1]}:'))

    writeCourierList()


def deleteCourier():
    courierList()
    courDel = input('\nCourier entry to delete:')

    courList.pop(courDel - 1)

    writeCourierList()


def writeCourierList():
    with open("couriers.csv", "w", newline = '') as change:
        writer = csv.DictWriter(change, fieldheads)
        writer.writeheader()
        writer.writerows(courList)
