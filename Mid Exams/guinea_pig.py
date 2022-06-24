quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
weight_guinea = float(input())

for i in range(1, 31):
    quantity_food -= 0.3
    if i % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if i % 3 == 0:
        quantity_cover -= (1 / 3) * weight_guinea
    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        print('Merry must go to the pet store!')
        break

if quantity_food > 0 and quantity_hay > 0 and quantity_cover > 0:
    print(f'Everything is fine! Puppy is happy! Food: {quantity_food:.2f}, Hay: {quantity_hay:.2f}, Cover: {quantity_cover:.2f}.')
