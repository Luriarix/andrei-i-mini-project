import csv
import os
import connection


def clear():
    os.system( 'cls' )


def fieldNames():
    sql_test = "show fields from courier"
    return connection.execute(sql_test)

def courierList():
    def allRows():
        sql = "SELECT * FROM courier"
        return connection.execute(sql)

    rowsValue = '' # stand in string for a row, so I can print it to the screen

    for i in allRows():
        z = 0 # I prefere the for(i) loop in C++, z stands in as a count
        for item in fieldNames():
            rowsValue += f'{item[0]}: {i[z]}     '
            z += 1
        print(rowsValue)
        rowsValue = ''


def addCourier():
    rowValues = "'Rob', 404"
    columnNames = ''
    z = 0 # standin for a count

    for item in fieldNames():
        columnNames += f"{item[0]}, "
        # if 'char' in item[1]:
        #     rowValues += "'" + (input(f'\nProduct {item[0]}:\n')) + "', "
        # else:
        #     rowValues += (input(f'\nProduct {item[0]}:\n')) + ", "
        z += 1

    sql = f"INSERT INTO courier ({columnNames.rstrip(',')}) VALUES ({rowValues.rstrip(',')}); "
    connection.execute(sql)


def print_to_screen_specific_courier(cour_id):
    sql = f"SELECT * FROM courier WHERE id = {cour_id}"
    i = connection.execute(sql)
    print(f'1 id: {i[0][0]}    2 Name: {i[0][1]}    3 Phone: {i[0][2]}\n')
    return i


def updateCourier():
    newValueSet = ''
    columns = fieldNames()

    courierList()
    updateCour = int(input('\n0: Cancel\nSelect courier to update:'))

    clear()
    if updateCour != 0:
        cour = print_to_screen_specific_courier(updateCour)
        whatToChange = int(input('0:Cancel     1:All columns     2:One specific column\n'))

        while True:
            if whatToChange == 1:
                z = 0 # standin for a count
                for item in columns:
                    newValue = input(f'New {item[0]}:')
                    if 'char' in item[1]:
                        newValueSet += f"{item[0]} = '{newValue}', "
                    else:
                        newValueSet += f"{item[0]} = {newValue}, "
                    z += 1

            elif whatToChange == 2:
                whichColumnToChange = int(input('Which column do you wanna change?  ')) - 1
                if 'char' in columns[whichColumnToChange][1]:
                    newValue = input(f'New {columns[whichColumnToChange][0]}:  ')
                    newValueSet = f"{columns[whichColumnToChange][0]} = '{newValue}'"
                else:
                    newValue = int(input(f'New {columns[whichColumnToChange][0]}:  '))
                    newValueSet = f"{columns[whichColumnToChange][0]} = {newValue}"

            elif whatToChange == 0:
                break

            else:
                print('Option invalid.')
                whatToChange = int(input('0:Cancel     1:All columns     2:One specific column\n'))

            if newValue == '':
                print("Dude you're missing something a.k.a The new value is empty? ")
                temp = int(input("0:Cancel     1:All columns     2:One specific column     Empty:Continue with original choice\n"))
                if temp == 0:
                    break
                elif temp != whatToChange and temp != '':
                    whatToChange = temp

        sql = f"UPDATE courier SET {newValueSet.rstrip(',')} WHERE id = {updateCour.rstrip(',')};"
        connection.execute(sql)


def deleteCourier():
    courierList()
    courDel = int(input('\nId of courier to delete:'))

    sql = f"DELETE from courier where id =  {courDel}"
    connection.execute(sql)