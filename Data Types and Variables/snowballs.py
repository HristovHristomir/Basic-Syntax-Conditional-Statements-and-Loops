snowballs = int(input())

highest_value = 0
high_weight = 0
high_time = 0
high_quality = 0

for i in range(1, snowballs + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight / time_needed) ** quality
    if value > highest_value:
        highest_value = value
        high_weight = weight
        high_time = time_needed
        high_quality = quality

print(f'{high_weight} : {high_time} = {int(highest_value)} ({high_quality})')
