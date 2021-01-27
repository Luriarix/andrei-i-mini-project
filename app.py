import os
import sys
from couriers import addCourier, courierList, deleteCourier, updateCourier
from products import addProduct, deleteProduct, productList, updateProduct


def clear():
    os.system( 'cls' )


product = False
courier = False


print('\nWelcome to the app!')


while True:
    if product == False and courier == False:
        print('\nEnter a number: \n0: Close   1: Product List   2: Courier List\n')

    elif product == True:
        print('\nEnter a number: \n0: Close   1: Product List   2: New Product   3: Update Product   4: Delete Product   5: Main Menu \n')

    elif courier == True:
        print('\nEnter a number: \n0: Close   1: Courier List   2: New Courier   3: Update Courier   4: Delete Courier   5: Main Menu \n')


    value = int(input("Select a menu option\n"))
    clear()
    if value == 0:
        sys.exit(0)

    elif value == 1 and ((product == False and courier == False) or product == True):
        # clear()
        print('\nCurrent Products:\n')
        productList()        
        product = True
    
    elif value == 1 and (courier == True and product == False):
        # clear()
        print('\nCurrent Couriers:\n')
        courierList()        

    elif value == 2 and (product == False and courier == False):
        # clear()
        print('\nCurrent Couriers:\n')
        courierList()
        courier = True

    elif value == 2 and product == True:
        # clear()
        addProduct()
        print('\nNew Product List:\n')
        productList()

    elif value == 2 and courier == True:
        # clear()
        addCourier()
        print('\nNew Courier List:\n')
        courierList()

    elif value == 3 and product == True:
        # clear()
        updateProduct()
        print('\nUpdated Product List:\n')
        productList()

    elif value == 3 and courier == True:
        # clear()
        updateCourier()
        print('\nUpdated Courier List:\n')
        courierList()

    elif value == 4 and product == True:
        # clear()
        deleteProduct()
        print('\nNew Product List:\n')
        productList()

    elif value == 4 and courier == True:
        # clear()
        deleteCourier()
        print('\nNew Courier List:\n')
        courierList()

    elif value == 5 and (product == True or courier == True):
        # clear()
        product = False
        courier = False

    else:
        print("Please select a value I'm familiar with.")
        if product == True:
            print('\nCurrent Products:\n')
            productList()
        elif courier == True:
            print('\nCurrent Couriers:\n')
            courierList()
