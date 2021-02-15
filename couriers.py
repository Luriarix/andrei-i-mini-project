import csv
import os
from connection import connection, cursor


def clear():
    os.system( 'cls' )


def fieldNames():
    sql_test = "show fields from courier"
    cursor.execute(sql_test)
    x = cursor.fetchall()
    return x


def courierList():
    def allRows():
        sql = "SELECT * FROM courier"
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


def addCourier():
    rowValues = "'Rob', 404"
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

    sql = f"INSERT INTO courier ({columnNames}) VALUES ({rowValues}); "
    cursor.execute(sql)
    connection.commit()


def print_to_screen_specific_courier(cour_id):
    sql = f"SELECT * FROM courier WHERE id = {cour_id}"
    cursor.execute(sql)
    i = cursor.fetchone()
    print(f'1 id: {i[0]}    2 Name: {i[1]}    3 Price: {i[2]}\n')
    return i


def updateCourier():
    courierList()

    newValueSet = ''
    columns = fieldNames()

    updateCour = int(input('\n0: Cancel\nSelect courier to update:'))

    clear()
    cour = print_to_screen_specific_courier(updateCour)

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
            newValueSet = f"{columns[whichColumnToChange][0]} = {newValue}"

    sql = f"UPDATE courier SET {newValueSet} WHERE id = {updateCour};"
    print(sql)
    # cursor.execute(sql)
    # connection.commit()


def deleteCourier():
    courierList()
    courDel = int(input('\nId of courier to delete:'))

    sql = f"DELETE from courier where id =  {courDel}"
    cursor.execute(sql)
    connection.commit()