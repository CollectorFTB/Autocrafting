class BaseItem:
    def __init__(self, name, id=0):
        self.id = id
        self.name = name
        
class Item(BaseItem):
     def __init__(self, name, recipe, id=0):
        super().__init__(name, id)
        self.recipe = recipe

class Recipe:
    def __init__(self, positions, quantity=1):
        self.positions = positions
        self.quantity = quantity

def create_item(name, id=0, recipe=None):
    if recipe:
        item = Item(name, recipe, id)
    else:
        item = BaseItem(name, id)
    
    return item
