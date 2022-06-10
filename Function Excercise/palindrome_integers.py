numbers = input().split(', ')


def palindrome_numbers():
    for num in numbers:
        reversed_num = str(num[::-1])
        if num == reversed_num:
            print('True')
        else:
            print('False')


palindrome_numbers()
