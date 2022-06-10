import math

sequence_of_numbers = input().split()


def min_max_sum():
    min_value = min(list(map(int, sequence_of_numbers)))
    max_value = max(list(map(int, sequence_of_numbers)))
    sum_digit = 0
    for digit in sequence_of_numbers:
        sum_digit += int(digit)
    print(f'The minimum number is {min_value}')
    print(f'The maximum number is {max_value}')
    print(f'The sum number is: {sum_digit}')


min_max_sum()
