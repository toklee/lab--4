items = {
    'r': {'size': 3, 'points': 25},
    'p': {'size': 2, 'points': 15},
    'a': {'size': 2, 'points': 15},
    'm': {'size': 2, 'points': 20},
    'i': {'size': 1, 'points': 5},
    'd': {'size': 1, 'points': 10},
    'k': {'size': 1, 'points': 15},
    'x': {'size': 3, 'points': 20},
    't': {'size': 1, 'points': 25},
    'f': {'size': 1, 'points': 15},
    's': {'size': 2, 'points': 20},
    'c': {'size': 2, 'points': 20},
}
sum = 0

def optimize_inventory(slots, illness, base_survival_points):
    inventory = []
    used_items = set()

    if illness:
        if illness == 'astma':
            inventory.append('i')
            used_items.add('i')
        else:
            inventory.append('d')
            used_items.add('d')
        slots -= 1
    else:
        items.pop('d')
        items.pop('i')
    sorted_items = sorted(items.items(), key=lambda x: x[1]['points'] / x[1]['size'], reverse=True)

    for item_code, item_data in sorted_items:
        if item_code in used_items:
            continue
        while slots >= item_data['size']:
            inventory.append(item_code)
            used_items.add(item_code)
            slots -= item_data['size']
            break

    inventory_matrix = []
    row = []
    for i, item in enumerate(inventory):
        row.append(item)
        if (i + 1) % 4 == 0:
            inventory_matrix.append(row)
            row = []
    if row:
        inventory_matrix.append(row)

    total_survival_points = base_survival_points
    for item in inventory:
        total_survival_points += items[item]['points']

    return inventory_matrix, total_survival_points


slots = 8
illness = False
base_survival_points = 15

inventory, total_survival_points = optimize_inventory(slots, illness, base_survival_points)

print("Инвентарь:")
for row in inventory:
    print(",".join(row))
print("\nИтоговые очки выживания:", total_survival_points)