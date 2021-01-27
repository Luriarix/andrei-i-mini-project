import sys
from products import productList

def main_menu():
    print('\nWelcome to the app!\n')
    print('Enter 0 to close, \nEnter 1 to show products\n')#Enter 2 to show Couriers\n')

    products = ['Coke', 'Sprite']

    while True:
        value = int(input("Select a menu option\n"))
        if value == 0:
            sys.exit(0)

        elif value == 1:
            print("\n")
            productList()

            for item in products:
                print(f"{item}".center(20))
                print("\n")