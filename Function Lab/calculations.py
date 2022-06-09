operator = input()
first_number = int(input())
second_number = int(input())


def calculation():
    if operator == 'multiply':
        result = first_number * second_number
        return result
    elif operator == 'divide':
        result = first_number / second_number
        return int(result)
    elif operator == 'add':
        result = first_number + second_number
        return result
    else:
        result = first_number - second_number
        return result


print(calculation())
