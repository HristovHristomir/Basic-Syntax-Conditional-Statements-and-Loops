some_text = input().split()

result = [num for num in some_text if len(num) % 2 == 0]

print(*result, sep='\n')
