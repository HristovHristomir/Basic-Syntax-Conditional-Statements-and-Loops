single_string = input()

opposite_list = [int(x.strip()) for x in single_string.split(' ')]
new_list = []

for i in range(len(opposite_list)):
    new_list.append(opposite_list[i] * - 1)

print(new_list)
