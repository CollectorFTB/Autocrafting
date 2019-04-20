import save

items = save.load_items()

def craft_item(item_name, quantity):
    requirements = get_requirements(item_name, quantity)
    print(requirements)
    for quantity, item_name in requirements:
        try:
            output[item_name] += quantity
        except KeyError:
            output[item_name] = quantity
    return output

def get_requirements(item_name, quantity):
    item = next((item for item in items if item.name == item_name), None)

    if item:
        re = list()
        try:
            for requirement in item.recipe.positions:
                positions, item_name = requirement
                re.append(get_requirements(item_name, quantity*len(positions)/item.recipe.quantity))
            return [requirement for requirements in re for requirement in requirements]
        except AttributeError:
            return [[quantity, item.name]]
    else:
        return "Item doesn't exist"