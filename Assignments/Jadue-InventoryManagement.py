# Brandon Jadue
# 4/2/24
# This program will manage inventory
import csv
import time

class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getQuantity(self):
        return self.__quantity

inventory = {}
#1
def addProduct():
    # user input
    key = input("Enter product name: ")
    price = input("Enter product price: ")
    quantity = input("Enter product quantity: ")

    curProd = Product(key, price, quantity)
    inventory[curProd.getName()] = {}
    inventory[curProd.getName()][curProd.getPrice()] = []
    inventory[curProd.getName()][curProd.getPrice()].append(curProd.getQuantity())
#2
def loadCSV(filename):
    count = 0
    with open(f'{filename}.csv', 'r') as loadInvCSV:
        csvReader = csv.DictReader(loadInvCSV)
        for row in csvReader:
            key = row["Product Name"]
            price = row["Price"]
            quantity = row["Quantity"]

            curProd = Product(key, price, quantity)
            inventory[curProd.getName()] = {}
            inventory[curProd.getName()][curProd.getPrice()] = []
            inventory[curProd.getName()][curProd.getPrice()].append(curProd.getQuantity())

            count += 1
    print(f'{filename}.csv has been loaded into the inventory with {count} item(s).')
#3
def invValue():
    totalVal = 0.00
    for product in inventory:
        for price in inventory[product]:
            x = float(price)
            for quantity in inventory[product][price]:
                y = int(quantity)
                totalVal += float(x * y)
    print(f"\nYour current inventory is worth ${totalVal:.2f}")
#5
def invAlert():
    count = 0
    items = []
    quant = []
    for product in inventory:
        for price in inventory[product]:
            for quantity in inventory[product][price]:
                if int(quantity) < 10:
                    items.append(str(product))
                    quant.append(int(quantity))
                    count += 1
    print(f"\nThe following {count} item(s) have less than 10 in stock")
    for i in range(count):
        print(f"{items[i]} - {quant[i]}")
#4
def showInventory():
    for product in inventory:
        print(f'\nName: {product}')
        for price in inventory[product]:
            print(f'Price: ${price}')
            for quantity in inventory[product][price]:
                print(f'Quantity: {quantity}')

def menu():
    print('\nPlease select an action.'
          '\n1. Add a product'
          '\n2. Load CSV file'
          '\n3. Calculate Inventory Value'
          '\n4. Show current inventory'
          '\n5. Stock quota check')
    usrChoice = input('\n(1-#)\n')
    return usrChoice

def main():
    print("Welcome to the inventory manager")
    goAgain = 'y'
    while goAgain.lower() == 'y':
        time.sleep(1)
        usrChoice = menu()
        if usrChoice == "1":
            addProduct()
        elif usrChoice == "2":
            filename = input('\nEnter the name of the CSV file you would like to use:\n')
            loadCSV(filename)
        elif usrChoice == "3":
            invValue()
        elif usrChoice == "4":
            showInventory()
        elif usrChoice == "5":
            invAlert()
        else:
            print("Invalid Option")






main()