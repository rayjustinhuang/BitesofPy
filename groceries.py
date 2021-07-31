import argparse
from collections import namedtuple

Item = namedtuple('Item', 'product price craving')


class Groceries:

    def __init__(self, items=None):
        """This cart can be instantiated with a list of namedtuple
           items, if not provided use an empty list"""
        self._items = items if items is not None else []

    def show(self, items=None):
        """Print a simple table of cart items with total at the end"""
        items = items if items is not None else self
        for item in items:
            product = f'{item.product}'
            if item.craving:
                product += ' (craving)'
            print(f'{product:<30} | {item.price:>3}')
        self._print_total(items)

    def _print_total(self, items):
        """Calculate and print total price of cart"""
        total = sum(item.price for item in items)
        print('-' * 36)
        print(f'{"Total":<30} | {total:>3}')

    def add(self, new_item):
        """Add a new item to cart, exceptions left out for simplicity"""
        self._items.append(new_item)
        self.show()

    def delete(self, product):
        """Delete item matching 'product', raises IndexError
           if no item matches"""
        for i, item in enumerate(self):
            if item.product == product:
                self._items.pop(i)
                break
        else:
            raise IndexError(f'{product} not in cart')
        self.show()

    def search(self, search):
        """Filters items matching insensitive 'contains' search, and passes
           them to show for printing"""
        items = [item for item in self if search.lower()
                 in item.product.lower()]
        self.show(items)

    @property
    def due(self):
        return sum(item.price for item in self)

    def __len__(self):
        """The len of cart"""
        return len(self._items)

    def __getitem__(self, index):
        """Making the class iterable (cart = Groceries() -> cart[1] etc)
           without this dunder I would get 'TypeError: 'Cart' object does
           not support indexing' when trying to index it"""
        return self._items[index]


def create_parser():
    """TODO 1
       Create an ArgumentParser object giving it the required options,
       note that the options are mutually exclusive. 
       Returns a argparse.ArgumentParser object"""
       
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--add', nargs=3, action='extend', help='add item providing name (str), price (int), and craving (bool)')
    parser.add_argument('-d','--delete', nargs=1, type=str, help='delete a product by name (str)')
    parser.add_argument('-l','--list', help='show items in cart', action = 'store_true')
    parser.add_argument('-s','--search', nargs = 1, help='search items by name')
    
    return parser
    pass


def handle_args(args=None, cart=None):
    """TODO 2
       Receives args and cart and performs the add/delete/list/search
       operations on cart:
       - If args not provided create a parser object and retrieve the args
       - If cart not provided make a Groceries object with 0 or more items
       Modifies the cart object, no return"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if cart is None:
        cart = Groceries()

    # different crud operations - please complete ...
    #print(vars(args).items())
    #print(args)
    for operation, etc in vars(args).items():
        if etc == None:
            continue
        elif operation == 'add':
            if len(etc) == 3:
                prod, price, craving = etc
                cart.add(Item(str(prod), int(price), bool(craving)))
        elif operation == 'delete':
            if len(etc) == 1:
                cart.delete(etc)
            else: raise SystemExit
        elif operation == 'list':
            cart.show()
        elif operation == 'search':
            cart.search(etc)
        else:
            raise SystemExit
            
            
"""
def crud_functions(operation, args):
    print(operation)
    print(args)
    if args == [None]:
        raise SystemExit
    elif operation == 'add':
        if len(args) == 3:
            prod, price, craving = args
            cart.add(Item(str(prod), int(price), bool(craving)))
    elif operation == 'delete':
        if len(args) == 1:
            cart.delete(args)
        else: raise SystemExit
    elif operation == 'list':
        cart.show()
    elif operation == 'search':
        cart.search(args)
    else:
        raise SystemExit
"""