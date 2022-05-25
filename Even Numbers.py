n = int(input())

flag = 0

for num in range(n):
    num = int(input())
    if (num % 2) != 0:
        print(f'{num} is odd!')
        break
    else:
        flag += 1

if flag == n:
    print('All numbers are even.')

