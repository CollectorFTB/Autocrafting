import save

items = save.load_items()

def craft_item(item_name, quantity):
    item = next((item for item in items if item.name == item_name), None)

    if item:
        re = list()
        try:
            for requirement in item.recipe.positions:
                positions, item_name = requirement
                re.append(craft_item(item_name, quantity*len(positions)/item.recipe.quantity))
            return re
        except AttributeError:
            return [quantity, item.name]
    else:
        return "Item doesn't exist"



        