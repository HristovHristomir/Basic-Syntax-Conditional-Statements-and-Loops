numbers = int(input())

sum = 0

for i in range(1, numbers + 1):
    letters = input()
    code = ord(letters)
    sum += code

print(f'The sum equals: {sum}')
