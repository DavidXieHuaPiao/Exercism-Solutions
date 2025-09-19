"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    dictionary = dict()
    while bool(items):
        element = items[0]
        times=items.count(element)
        dictionary[element]= times
        for i in range (times):
            items.remove(element)

    return dictionary
            


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    list_inventory = list(inventory.items())
    for i in list_inventory:
        for x in range(i[1]):
            items.append(i[0])
    new_dict = create_inventory(items)
    return new_dict


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for i in items:
        try:
            if inventory[i]>0:
                inventory[i]-=1
        except:
            continue
    return inventory


def remove_item(inventory, item):
    try:
        inventory.pop(item)
    except:
        None
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    a = list(inventory.items())
    for i in a:
        if i[1]<=0:
            a.remove(i)
    return a
