shopping_list = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break

    command = command.split()
    if command[0] == 'Urgent':
        if command[1] in shopping_list:
            continue
        else:
            shopping_list.insert(0, command[1])
    elif command[0] == 'Unnecessary':
        if command[1] in shopping_list:
            for i in shopping_list:
                if command[1] == i:
                    shopping_list.remove(i)
    elif command[0] == 'Correct':
        for i in range(len(shopping_list)):
            if shopping_list[i] == command[1]:
                shopping_list[i] = command[2]
    else:
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])

print(*shopping_list, sep=', ')
