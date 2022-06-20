numbers = list(map(int, input().split(', ')))

positive = [pos for pos in numbers if pos >= 0]
negative = [neg for neg in numbers if neg < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print(f'Positive: ', end='')
print(*positive, sep=', ')
print(f'Negative: ', end='')
print(*negative, sep=', ')
print(f'Even: ', end='')
print(*even, sep=', ')
print(f'Odd: ', end='')
print(*odd, sep=', ')
