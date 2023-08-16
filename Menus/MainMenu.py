import cmdOptions.Controller as Contr
from ItemHandling.Cart import Cart
from ItemHandling.Item import Item
import os

class MainMenu:

    def __init__(self) -> None:
        self._menu = Contr.Controller()
        self._cart = Cart()
        self.createMenu()
    
    def createMenu(self):
        self._menu.addOption("Add Item", self.addItem)
        self._menu.addOption("Remove Item", self.removeItem)
        self._menu.addOption("List Items", self.listItems)
        self._menu.addOption("Total Item Prices", self.itemPrices)

    @staticmethod
    def waitForEnter():
        input("\nPress enter to continue.....")

    @staticmethod
    def clearScreen():
        os.system("cls")

    def run(self):
        MainMenu.clearScreen()
        self._menu.runLoop()

    def addItem(self):
        MainMenu.clearScreen()

        print("Items in your Cart:\n")
        self._cart.printItems()

        if self._cart.is_empty():
            self._cart.noItemPrint()
            print("\n")

        name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        quantity = int(input("Enter Item quantity: "))
        discount = float(input("Enter discount (.15 = 15%): "))

        self._cart.addItem(Item(name, item_price, quantity, discount))

        MainMenu.clearScreen()

    def removeItem(self):
        MainMenu.clearScreen()

        print("Items in your Cart:\n")
        self._cart.printItems()
        name = input("\nEnter item name to remove: ")
        self._cart.removeItem(name)

        MainMenu.clearScreen()

    def listItems(self):
        MainMenu.clearScreen()

        print("Items in your Cart:\n")
        self._cart.printItems()
        MainMenu.waitForEnter()

        MainMenu.clearScreen()

    def itemPrices(self):
        MainMenu.clearScreen()

        self._cart.printItems()
        print(f"\nTotal Price: ${self._cart.ringUpItems()}")
        MainMenu.waitForEnter()

        MainMenu.clearScreen()