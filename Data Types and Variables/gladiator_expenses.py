lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
shield_count = 0

for i in range(1, lost_fight + 1):
    if i % 2 == 0:
        total_expenses += helmet_price
    if i % 3 == 0:
        total_expenses += sword_price
        if i % 2 == 0:
            total_expenses += shield_price
            shield_count += 1
            if shield_count % 2 ==0:
                total_expenses += armor_price
                
print(f'Gladiator expenses: {total_expenses:.2f} aureus')
