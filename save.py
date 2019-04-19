import json
import os
from item import Item, Recipe, create_item


SAVEDIR = "data.json"

def serialize(item):
    item_dict = vars(item)
    try:
        item_dict['recipe'] = vars(item.recipe)
    except AttributeError:
        pass
    return item_dict

def unserialize(item):
    item = create_item(**item)
    try:
        item.recipe = Recipe(**item.recipe)
    except AttributeError:
        pass
    return item

def save_items(items):
    items_str = [serialize(item) for item in items]
    with open(SAVEDIR, 'w') as json_file:
        json.dump(items_str, json_file)


def load_items():
    with open(SAVEDIR, 'r') as json_file:
        data = json.load(json_file)

    items = [unserialize(item) for item in data]
    return items

def init_items():
    if os.path.isfile(SAVEDIR):
        return load_items()
    else:
        return list()

def housekeeping(func):
    def wrapper():
        items = init_items()
        func(items)
        save_items(items)
    return wrapper