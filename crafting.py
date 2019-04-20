import save
from item import Item
from typing import List, Dict
from more_itertools import flatten
from itertools import groupby
from collections import defaultdict,Counter
items :List[Item] = save.load_items()

def craft_item(item_name, quantity=1) -> Dict[str, int]:
    requirements = list(get_requirements(item_name, quantity))
    
    output = defaultdict(int)
    for quantity, item_name in requirements:
        output[item_name] += quantity
    
    return dict(output)

def get_requirements(item_name:str, quantity:int) -> List[List[Item]]:
    item = next((item for item in items if item.name == item_name), None)

    if item:
        if item.recipe:
            return flatten([get_requirements(item_name, quantity*len(positions)/item.recipe.quantity) for positions, item_name in item.recipe.positions])
        else:
            return [[quantity, item.name]]
    else:
        raise Exception("Item doesn't exist: " + item_name)

