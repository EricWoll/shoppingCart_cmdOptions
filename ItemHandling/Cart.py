from ItemHandling.Item import Item

class Cart:

    def __init__(self):
        self._cart = list()

    def addItem(self, item: Item):
        self._cart.append(item)

    def removeItem(self, item_name: str) -> bool:
        sucess = False

        for index, item in enumerate(self._cart):
            if item_name == item.name:
                self._cart.pop(index)
                sucess = True

        return sucess
    
    def clearcart(self):
        self._cart.clear()

    def is_empty(self) -> bool:
        empty = True
        if len(self._cart) > 0:
            empty = False
        return empty
    
    def noItemPrint(self):
        print(f"{' ': <4} {'...': <15} {'...': <15} {'...': <15} {'...'}")
    
    def printItems(self):
        print(f"{' ': <4} {'Name': <15} {'Price': <15} {'discount': <15} {'Quantity'}")
        for index, item in enumerate(self._cart):
            print(f'{index + 1}. {" ":>1} {item.name: <15} ${item.item_price: <14.2f} {item.discount * 100: <.0f}{"%": <13} {item.quantity}')
    
    def ringUpItems(self):
        total = 0
        for item in self._cart:
            total += ( (item.item_price - item.discount * item.item_price) * item.quantity)
            
        return total