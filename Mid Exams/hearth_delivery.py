even_list = list(map(int, input().split('@')))

current_index = 0
failed_places = 0
check_list = []

while True:
    command = input()
    if command == 'Love!':
        break
    command = command.split()
    if int(command[1]) + current_index < len(even_list):
        current_index = int(command[1]) + current_index
        if even_list[current_index] > 0:
            even_list[current_index] -= 2
            if even_list[current_index] == 0:
                print(f'Place {current_index} has Valentine\'s day.')
        else:
            print(f'Place {current_index} already had Valentine\'s day.')

            check_list.append(current_index)
    else:
        current_index = 0
        if even_list[current_index] > 0:
            even_list[current_index] -= 2
            if even_list[current_index] == 0:
                print(f'Place {current_index} has Valentine\'s day.')
        else:
            print(f'Place {current_index} already had Valentine\'s day.')

for i in even_list:
    if i > 0:
        failed_places += 1

print(f'Cupid\'s last position was {current_index}.')
if failed_places == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {failed_places} places.')
