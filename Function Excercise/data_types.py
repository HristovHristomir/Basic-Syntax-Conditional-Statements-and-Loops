command = input()
number = input()


def data_type():
    if command == 'int':
        result = int(number) * 2
        print(result)
    elif command == 'real':
        result = float(number) * 1.5
        print(f'{result:.2f}')
    else:
        print(f'${number}$')


data_type()
