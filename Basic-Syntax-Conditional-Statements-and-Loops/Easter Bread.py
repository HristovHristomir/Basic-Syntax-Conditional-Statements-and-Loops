budget = float(input())
price_per_kilo = float(input())

price_pack_eggs = price_per_kilo * 0.75
price_milk = price_per_kilo * 1.25

total_loaves = 0
colored_eggs = 0

while budget > 0:
    loaf = price_pack_eggs + price_per_kilo + (price_milk / 4)
    if budget < loaf:
        break
    budget -= loaf
    total_loaves += 1
    colored_eggs += 3
    if total_loaves % 3 == 0:
        colored_eggs -= total_loaves - 2
        if colored_eggs < 0:
            colored_eggs = 0


print(f'You made {total_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

