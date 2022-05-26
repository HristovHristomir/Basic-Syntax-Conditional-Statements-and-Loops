orders = int(input())

total_price = 0

for i in range(1, orders + 1):
    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if 1 > capsule_per_day or capsule_per_day > 2000 or 0.01 > capsule_price or capsule_price > 100.00 or 1 > days or days > 31:
        continue
    price = capsule_price * days * capsule_per_day
    if price > 0:
        print(f'The price for the coffee is: ${price:.2f}')
    else:
        continue
    total_price += price

print(f'Total: ${total_price:.2f}')
