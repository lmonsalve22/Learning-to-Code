
def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print(f'Total number of items: {item_total}')

def add_to_inventory(inventory, addedItems):
    for key, value in list(inventory.items()):
        for i in addedItems:
            if i == key:
                inventory[key] = value + addedItems.count(i)
            else:
                inventory.setdefault(i, addedItems.count(i))

    display_inventory(inventory)


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
addedItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inventory, addedItems)