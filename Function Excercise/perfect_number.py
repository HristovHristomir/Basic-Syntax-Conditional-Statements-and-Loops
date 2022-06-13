number = int(input())


def aliquiot_sum():
    aliquiot_sum = 0
    for i in range(number - 1, 0, - 1):
        if number % i == 0:
            aliquiot_sum += i
    if aliquiot_sum == number:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


aliquiot_sum()
