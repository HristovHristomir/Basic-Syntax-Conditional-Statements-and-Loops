num = int(input())


def loading_bar():
    if num == 100:
        print('100% Complete!')
        print('[' + 10 * '%' + ']')
    else:
        print(f'{num}% ' + '[' + (num // 10) * '%' + int(10 - num // 10) * '.' + ']')
        print('Still loading...')


loading_bar()
