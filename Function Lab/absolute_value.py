import math

list_of_string = input().split()
list_of_absolute_value = []


def return_absolute_value():
    for n in list_of_string:
        number = abs(float(n))
        list_of_absolute_value.append(number)

    print(list_of_absolute_value)


return_absolute_value()
