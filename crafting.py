import save
from item import Item
from typing import List

items :List[Item] = save.load_items()

def craft_item(item_name, quantity=1):
    requirements = get_requirements(item_name, quantity)
    output = dict()
    for quantity, item_name in requirements:
        try:
            output[item_name] += quantity
        except KeyError:
            output[item_name] = quantity
    print(output)
    return output

def get_requirements(item_name:str, quantity:int) -> List[List[Item]]:
    item = next((item for item in items if item.name == item_name), None)

    if item:
        if item.recipe:
            re = [get_requirements(item_name, quantity*len(positions)/item.recipe.quantity) for positions, item_name in item.recipe.positions]
            return [requirement for requirements in re for requirement in requirements]
        else:
            return [[quantity, item.name]]
    else:
        raise Exception("Item doesn't exist: " + item_name)

