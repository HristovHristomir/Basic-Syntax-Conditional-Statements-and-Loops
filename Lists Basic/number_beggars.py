first_line = input()
second_line = int(input())

my_list = first_line.split(', ')
sum_of_numbers = 0
count_list = [0]*second_line


for i in range(0, len(count_list)):
    for j in range(i, len(my_list), second_line):
        count_list[i] += int(my_list[j])

print(count_list)
