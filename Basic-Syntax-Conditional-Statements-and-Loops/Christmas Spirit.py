quantity_decoration = int(input())
days_left_until_christmas = int(input())

total_price = 0
points = 0

for i in range(1, days_left_until_christmas + 1):
    if i % 11 == 0:
        quantity_decoration += 2
    if i % 2 == 0:
        total_price += 2 * quantity_decoration
        points += 5
    if i % 3 == 0:
        total_price += 8 * quantity_decoration
        points += 13
    if i % 5 == 0:
        total_price += 15 * quantity_decoration
        points += 17
    if i % 3 == 0 and i % 5 == 0:
        points += 30
    if i % 10 == 0:
        points -= 20
        total_price += 23
    if i % 10 == 0 and i == days_left_until_christmas:
        points -= 30

print(f'Total cost: {total_price}')
print(f'Total spirit: {points}')
