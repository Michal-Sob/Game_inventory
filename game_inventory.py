
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.

inventory = {'rope': 1, 'torch': 6, 'blanket': 3}
def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6
    '''
    for key, value, in inventory.items():
        print(f"{key}: {value}")


def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:
    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------
    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''
    item_title = "item name"
    item_count = "count"
    seperator = " | "
    dash_char = "-"
    max_width_item = max([len(str(item)) for item in inventory.keys()] + [len(item_title)])
    max_width_count = max([len(str(count)) for count in inventory.values()] + [len(item_count)])
    horizontal_dashes = dash_char * (max_width_item + max_width_count + len(seperator))
# header
    print(horizontal_dashes)
    print(f"{item_title:>{max_width_item}}{seperator}{item_count:>{max_width_count}}")
    print(horizontal_dashes)
# rows
    inventory_items = []
    if order == "count,desc":
        inventory_items = sorted(inventory.items(), key=lambda tuple: tuple[1], reverse=True)
    elif order == "count,asc":
        inventory_items = sorted(inventory.items(), key=lambda tuple: tuple[1], reverse=False)
    else:
        inventory_items = inventory.items()

    for item, count in inventory_items:
        print(f"{item:>{max_width_item}}{seperator}{count:>{max_width_count}}")
# footer
    print(horizontal_dashes)



def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''
    try:
        with open(filename, "r") as my_file:
            items = my_file.read()
            add_to_inventory(inventory, items.split(","))
    except FileNotFoundError:
        print(f"File '{filename}' not found!")



def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''
    item_list = []

    for item, ammount in inventory.items():
        for i in range(ammount):
            item_list.append(item)

    item_list = ','.join(item_list)

    try:
        with open(filename, 'w') as file:
            file.write(item_list)
    except PermissionError:
        print("You don't have permission creating file '/nopermission.csv'!")
