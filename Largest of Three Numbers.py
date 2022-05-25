first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number:
    if first_number > third_number:
        print(first_number)
    else:
        print(third_number)
else:
    if second_number > third_number:
        print(second_number)
    else:
        print(third_number)

# max_number = max(first_number, second_number, third_number)
# print(max_number)
