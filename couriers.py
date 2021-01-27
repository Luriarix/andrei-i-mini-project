
def courierList():
    couriers = open("couriers.txt", "r") #['Luke', 'Sam']

    for courier in couriers:
        print(f"{courier}".rstrip())

    couriers.close()


def addCourier():
    adding = open("couriers.txt", "a")
    adding.write(input('\nName of the new courier:\n')+"\n")
    adding.close()


def updateCourier():
    couriers = open("couriers.txt", "r")
    courList = []

    courChange = input('\nCourier name to change:\n')
    newCour = input('\nNew Courier name:\n')

    for item in couriers:
        courList.append(f"{item}".rstrip())

    try:
        courList.index(courChange)
    except ValueError:
        print("There is no such courier!\n")

    couriers.close()
    change = open("couriers.txt", "w")

    for item in courList:
        if item == courChange:
            change.write(newCour + "\n")
        else:
            change.write(item + "\n")

    change.close()


def deleteCourier():
    couriers = open("couriers.txt", "r")
    courList = []

    courDel = input('\nProduct to delete:\n')

    for item in couriers:
        if item != courDel + "\n":
            courList.append(item)

    couriers.close()
    change = open("couriers.txt", "w")

    for item in courList:
        change.write(item)

    change.close()