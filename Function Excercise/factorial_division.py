num1 = int(input())
num2 = int(input())


def factorial():
    fact1 = num1
    fact2 = num2
    result = 0
    for i in range(1, num1):
        fact1 *= i
    for i in range(1, num2):
        fact2 *= i
    if num1 == 0:
        fact1 = 1
    if num2 == 0:
        fact2 = 1
    result = fact1 / fact2
    print(f'{result:.2f}')


factorial()
