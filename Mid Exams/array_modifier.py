initial_array = list(map(int, input().split()))

command = input()

while command != 'end':
    command = command.split()
    if command[0] == 'swap':
        initial_array[int(command[1])], initial_array[int(command[2])] \
            = initial_array[int(command[2])], initial_array[int(command[1])]
    elif command[0] == 'multiply':
        initial_array[int(command[1])] = initial_array[int(command[1])] * initial_array[int(command[2])]
    else:
        for i in range(0, len(initial_array)):
            initial_array[i] -= 1
    command = input()

print(*initial_array, sep=', ')
