from dataclasses import dataclass

@dataclass
class Item:
    '''
    Class for keeping track of an item in the Shopping Cart
    '''
    name: str
    item_price: float
    quantity: int
    discount: float