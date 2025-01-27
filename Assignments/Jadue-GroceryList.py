# Brandon Jadue
# 11/10/23
# This program will create a shopping list for the user.
import time
global groceryFile
listTotal = 0.00
def createList():
    global groceryFile
    try:
        groceryFile = open(f"{usrListName}_gList.txt", "r")
        groceryFile.close()
        groceryFile = open(f"{usrListName}_gList.txt", "a")
        print(f"Adding onto grocery list {usrListName}.")
    except FileNotFoundError:
        groceryFile = open(f"{usrListName}_gList.txt", "w")
        groceryFile.write(f"Grocery List - {usrListName.upper()}")
        groceryFile.close()
        groceryFile = open(f"{usrListName}_gList.txt", "a")
        print("Grocery list has been created.")
    groceryFile.write("\n------------------------------")
def newItem():
    global groceryFile
    curItemName = input(f"\nWhat is item {i}: ")
    try:
        curItemQuant = int(input(f"What is the quantity of {curItemName} you are planning on buying?: "))
        curItemPrice = float(input(f"How much does {curItemName} cost?: "))
    except ValueError:
        print("\nAn error has occurred. Please enter a proper value.")
    groceryFile.write(f"\n{i:<}. {curItemName:<6}   {curItemQuant:^5}    ${curItemPrice * curItemQuant:.2f} (${curItemPrice:.2f})")
    return float(curItemPrice * curItemQuant)


usrListName = input("Enter grocery list name to edit/create: ")
# creates or calls list. if list does not exist, file is created.
# if list does exist, file is called to append
createList()
try:
    usrItemCount = int(input("How many groceries are you planning to buy?: "))
except ValueError:
    print("Error! Please enter a number for how many groceries you are buying.")
    groceryFile.write("\nAn error has occurred while writing to file. :(")
    groceryFile.close()
    time.sleep(2)

for i in range(1, usrItemCount+1):
    cost = newItem()
    listTotal += cost

groceryFile.write(f"\n------------------------------\nTOTAL               ${listTotal:.2f}")
print(f"\nSuccessfully written to {usrListName}_gList.txt")
groceryFile.close()

# Note to Professor Krepshaw - This is here because I tend to
# test my scripts in the command line as well as PyCharm.
time.sleep(3)