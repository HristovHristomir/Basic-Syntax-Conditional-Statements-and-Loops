product = input()
quantity = int(input())


def total_price():
    if product == 'coffee':
        total_price = quantity * 1.50
    elif product == 'water':
        total_price = quantity * 1.00
    elif product == 'coke':
        total_price = quantity * 1.40
    else:
        total_price = quantity * 2.00
    return f'{total_price:.2f}'


print(total_price())
