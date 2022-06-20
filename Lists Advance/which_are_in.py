first_list = input().split(', ')
second_list = input().split(', ')

result_list = []

for word in first_list:
    for substring in second_list:
        if word in substring:
            result_list.append(word)
            break

print(result_list)
