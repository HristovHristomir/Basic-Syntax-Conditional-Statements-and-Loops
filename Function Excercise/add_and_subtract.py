num1 = int(input())
num2 = int(input())
num3 = int(input())


def sum_numbers():
    sum = num1 + num2
    return sum


def subtract():
    sub = sum_numbers() - num3
    return sub


def add_and_subtract():
    print(subtract())


add_and_subtract()
