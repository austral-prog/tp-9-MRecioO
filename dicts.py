def create_inventory(items):
    inventory = dict()
    for elem in set(items):
        elem_count = items.count(elem)
        inventory[elem] = elem_count
    return inventory


def add_items(inventory, items):
    lestat = list()
    if inventory != {}:
        for key in inventory.keys():
            cant = inventory[key]
            for i in range(0,cant):
                lestat.append(key)
        return create_inventory(lestat + items)
    else:
        return create_inventory(items)

def decrement_items(inventory, items):
    dic = dict()
    inventarios = create_inventory(items)
    for key in inventarios.keys():
        num = inventory[key] - inventarios[key]
        if num < 0: num = 0
        dic[key] = num
    return dic

def remove_item(inventory, item):
    if item in inventory.keys():
        del inventory[item]
    return inventory


def list_inventory(inventory):
    tuple_list = list()
    for key in inventory.keys():
        if inventory[key] > 0:
            tuple_list.append((key, inventory[key]))
    return tuple_list
