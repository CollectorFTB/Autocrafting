import save
from crafting import craft_item
from item import Item, Recipe

@save.housekeeping
def main(items):
    items.append(Item('oak wood'))
    items.append(Item('oak wood planks', Recipe([[[0], 'oak wood']], 4)))
    items.append(Item('chest', Recipe([[[0, 1, 2, 3, 5, 6, 7 ,8], 'oak wood planks']], 1)))
    print(craft_item(items, 'chest', 2))

if __name__ == '__main__':
    main()
