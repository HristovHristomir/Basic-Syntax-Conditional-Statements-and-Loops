programming_basic = {}
fundamentals = {}
advanced = {}
others = {}
command = ''

while True:
    command = input().split(':')
    if len(command) == 1:
        command = command
        break

    if command[2] == 'programming basics':
        programming_basic.update({command[0]: command[1]})
    elif command[2] == 'fundamentals':
        fundamentals.update({command[0]: command[1]})
    elif command[2] == 'advanced':
        advanced.update({command[0]: command[1]})
    else:
        others.update({command[0]: command[1]})

if command[0] == 'programming_basics':
    for k, v in programming_basic.items():
        print(f'{k} - {v}')
elif command[0] == 'fundamentals':
    for k, v in fundamentals.items():
        print(f'{k} - {v}')
elif command[0] == 'advanced':
    for k, v in advanced.items():
        print(f'{k} - {v}')
else:
    for k, v in others.items():
        print(f'{k} - {v}')
