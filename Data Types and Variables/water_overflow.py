number_of_inputs = int(input())

capacity = 0

for i in range(1, number_of_inputs + 1):
    pouring_water = int(input())
    capacity += pouring_water
    if capacity > 255:
        print('Insufficient capacity!')
        capacity -= pouring_water
        continue

print(capacity)
