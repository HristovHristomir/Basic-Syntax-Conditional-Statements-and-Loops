sequence_of_integers = list(map(int, input().split()))
command = input()
count_list = []

while command != 'End':
    count_list.append(command)
    if int(command) > (len(sequence_of_integers) - 1):
        command = input()
        continue
    for index in range(0, len(sequence_of_integers)):
        if index != int(command):
            if sequence_of_integers[index] > sequence_of_integers[int(command)]:
                sequence_of_integers[index] -= sequence_of_integers[int(command)]
            else:
                sequence_of_integers[index] = sequence_of_integers[int(command)] + sequence_of_integers[index]
    sequence_of_integers[int(command)] = - 1

    command = input()

count_list = list(filter(lambda x: int(x) < len(sequence_of_integers), count_list))
count_list = list(map(int, count_list))

for i in count_list:
    sequence_of_integers[i] = - 1


print(f'Shot targets: {len(count_list)} ->', end=' ')
print(*sequence_of_integers, sep=' ')
