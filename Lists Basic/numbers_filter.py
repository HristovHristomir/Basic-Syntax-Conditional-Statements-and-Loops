n = int(input())

number_list = []
filtered_list = []

for i in range(n):
    num = int(input())
    number_list.append(num)

command = input()

if command == 'even':
    for i in number_list:
        if i % 2 == 0:
            filtered_list.append(i)
elif command == 'odd':
    for i in number_list:
        if i % 2 != 0:
            filtered_list.append(i)
elif command == 'positive':
    for i in number_list:
        if i >= 0:
            filtered_list.append(i)
elif command == 'negative':
    for i in number_list:
        if i < 0:
            filtered_list.append(i)


print(filtered_list)
