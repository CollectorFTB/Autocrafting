import json
import os
from item import Item, Recipe


SAVEDIR = "data.json"

def serialize(item):
    item_dict = vars(item)
    if item.recipe:
        item_dict['recipe'] = vars(item.recipe)
    return item_dict

def unserialize(item):
    item = Item(**item)
    if item.recipe:
        item.recipe = Recipe(**item.recipe)
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