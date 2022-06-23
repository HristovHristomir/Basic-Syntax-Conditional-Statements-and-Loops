sequence_of_integers = list(map(int, input().split()))

average_value = sum(sequence_of_integers) / len(sequence_of_integers)

bigger_numbers = list(filter(lambda x: x > average_value, sequence_of_integers))
bigger_numbers = sorted(bigger_numbers, key=lambda x: -x)

if bigger_numbers:
    print(*bigger_numbers[0:5], sep=' ')
else:
    print('No')
