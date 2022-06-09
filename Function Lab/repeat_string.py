my_string = input()
counter = int(input())


def repeat_string():
    repeat_string = lambda a, b: a * b
    result = repeat_string(my_string, counter)
    print(result)


repeat_string()
