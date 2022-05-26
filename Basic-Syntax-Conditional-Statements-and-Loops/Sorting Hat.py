name = ''

flag = True

while name != 'Welcome!':
    name = input()
    if name == 'Welcome!':
        break
    if name == 'Voldemort':
        flag = False
        print('You must not speak of that name!')
        break
    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    else:
        print(f'{name} goes to Hufflepuff.')


if flag is True:
    print('Welcome to Hogwarts.')
