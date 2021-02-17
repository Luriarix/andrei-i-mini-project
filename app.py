import os
import sys
from products import addProduct, deleteProduct, productList, updateProduct
from couriers import addCourier, courierList, deleteCourier, updateCourier
from order import addOrder, deleteOrder, orderList, updateOrder
import connection


def clear():
    os.system( 'cls' )

# Global variabels to keep track in what menu I'm in + start of the app
product = False
courier = False
order = False

print('\nWelcome to the app!')


while True:
# Main Menu
    if product == False and courier == False and order == False:
        print('\nEnter a number:\
    \n0: Close\
    1: Product List\
    2: Courier List\
    3: Order List\n')

# Prod Menu
    elif product == True:
        print('\nEnter a number:\
    \n0: Close\
    1: Product List\
    2: New Product\
    3: Update Product\
    4: Delete Product\
    5: Main Menu \n')

# Courier Menu
    elif courier == True:
        print('\nEnter a number:\
    \n0: Close\
    1: Courier List\
    2: New Courier\
    3: Update Courier\
    4: Delete Courier\
    5: Main Menu \n')

# Order Menu
    elif order == True:
        print('\nEnter a number:\
    \n0: Close\
    1: Order List\
    2: New Order\
    3: Update Order\
    4: Delete Order\
    5: Main Menu \n')

#Main options
    value = int(input("Select a menu option: "))
    print('\n')

    if value == 0:
        # cursor.close()
        connection.connection.close()
        sys.exit(0)

    elif value == 1 and ((product == False and courier == False and order == False) or product == True):
        clear()
        print('\nCurrent Products:\n')
        productList()
        product = True

    elif value == 2 and (product == False and courier == False and order == False):
        clear()
        print('\nCurrent Couriers:\n')
        courierList()
        courier = True

    elif value == 3 and (product == False and courier == False and order == False):
        clear()
        print('\nCurrent Orders:\n')
        orderList()
        order = True

    elif value == 5 and (product == True or courier == True or order == True):
        clear()
        product = False
        courier = False
        order = False

#Product options
    elif value == 2 and product == True:
        addProduct()
        clear()
        print('\nNew Product List:\n')
        productList()

    elif value == 3 and product == True:
        clear()
        updateProduct()
        clear()
        print('\nUpdated Product List:\n')
        productList()

    elif value == 4 and product == True:
        deleteProduct()
        clear()
        print('\nNew Product List:\n')
        productList()

#Couriers options
    elif value == 1 and (courier == True and product == False and order == False):
        clear()
        print('\nCurrent Couriers:\n')
        courierList()

    elif value == 2 and courier == True:
        addCourier()
        clear()
        print('\nNew Courier List:\n')
        courierList()

    elif value == 3 and courier == True:
        clear()
        updateCourier()
        clear()
        print('\nUpdated Courier List:\n')
        courierList()

    elif value == 4 and courier == True:
        deleteCourier()
        clear()
        print('\nNew Courier List:\n')
        courierList()

#Orders options
    elif value == 1 and (order == True and product == False and courier == False):
        clear()
        print('\nCurrent Orders:\n')
        orderList()

    elif value == 2 and order == True:
        clear()
        addOrder()
        print('\nNew Order List:\n')
        orderList()

    elif value == 3 and order == True:
        clear()
        updateOrder()
        orderList()

    elif value == 4 and order == True:
        clear()
        deleteOrder()
        orderList()

#In case something is introduced that it doesn't know what to do with it while in not in a different file (e.g. products.py, couriers,py and orders.py)
    else:
        clear()
        print("Please select a value I'm familiar with.")
        if product == True:
            print('\nCurrent Products:\n')
            productList()
        elif courier == True:
            print('\nCurrent Couriers:\n')
            courierList()
        elif order == True:
            print('\nCurrent Orders:\n')
            orderList()
