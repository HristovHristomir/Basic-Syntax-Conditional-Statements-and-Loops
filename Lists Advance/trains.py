number = int(input())
wagons = [0] * number

while True:
    command = input().split()

    if command[0] == 'add':
        wagons[-1] += int(command[1])
    elif command[0] == 'insert':
        wagons[int(command[1])] = wagons[int(command[1])] + int(command[2])
    elif command[0] == 'leave':
        wagons[int(command[1])] = wagons[int(command[1])] - int(command[2])
    else:
        break

print(wagons)
