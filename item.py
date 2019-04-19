class BaseItem:
    def __init__(self, name):
        self.name = name
        
class Item(BaseItem):
     def __init__(self, name, recipe):
        super().__init__(name)
        self.recipe = recipe

class Recipe:
    def __init__(self, positions, quantity=1):
        self.positions = positions
        self.quantity = quantity

def create_item(name, recipe=None):
    if recipe:
        item = Item(name, recipe)
    else:
        item = BaseItem(name)
    
    return item
