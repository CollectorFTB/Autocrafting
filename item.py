from typing import Optional,NamedTuple


class Recipe:
    def __init__(self, positions, quantity=1):
        self.positions = positions
        self.quantity = quantity


class Item:
    def __init__(self, name: str, recipe: Optional[Recipe]=None):
        self.name = name
        self.recipe = recipe
