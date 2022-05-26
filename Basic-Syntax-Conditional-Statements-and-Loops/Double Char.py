string = ''

while string != 'End':
    string = input()
    if string == 'End':
        break
    for i in string:
        if string == 'SoftUni':
            break
        print(i * 2, end='')
    if string == 'SoftUni':
        continue
    else:
        print()
