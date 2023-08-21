import cmdOptions.Controller as Contr
from cmdOptions.Tools import Tools
from ItemHandling.Cart import Cart
from ItemHandling.Item import Item
import os

class MainMenu:

    def __init__(self, os_type) -> None:
        self._menu = Contr.Controller()
        self._cart = Cart()
        self.createMenu()
        self.os_type = os_type
    
    def createMenu(self):
        self._menu.addOption("Add Item", self.addItem)
        self._menu.addOption("Remove Item", self.removeItem)
        self._menu.addOption("List Items", self.listItems)
        self._menu.addOption("Total Item Prices", self.itemPrices)

    def run(self):
        Tools.clearScreen(self.os_type)
        self._menu.runLoop()

    def addItem(self):
        Tools.clearScreen(self.os_type)

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

        Tools.clearScreen(self.os_type)

    def removeItem(self):
        Tools.clearScreen(self.os_type)

        print("Items in your Cart:\n")
        self._cart.printItems()
        name = input("\nEnter item name to remove: ")
        self._cart.removeItem(name)

        Tools.clearScreen(self.os_type)

    def listItems(self):
        Tools.clearScreen(self.os_type)

        print("Items in your Cart:\n")
        self._cart.printItems()
        Tools.waitForEnter()

        Tools.clearScreen(self.os_type)

    def itemPrices(self):
        Tools.clearScreen(self.os_type)

        self._cart.printItems()
        print(f"\nTotal Price: ${self._cart.ringUpItems()}")
        Tools.waitForEnter()

        Tools.clearScreen(self.os_type)