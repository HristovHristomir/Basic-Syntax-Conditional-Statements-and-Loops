products_inventory = {}

while True:
    command = input()
    if command == 'statistics':
        break

    command = command.split(': ')
    products = command[0]
    quantity = int(command[1])

    if products not in products_inventory:
        products_inventory[products] = quantity
    else:
        products_inventory[products] += quantity

print('Products in stock:')
products_representation = [f'- {item}: {str(products_inventory[item])}' for item in products_inventory]
print('\n'.join(products_representation))
print(f'Total Products: {len(products_inventory)}')
print(f'Total Quantity: {sum(products_inventory.values())}')
