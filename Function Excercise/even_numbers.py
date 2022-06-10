sequence_of_numbers = input().split()


def even_numbers():
    even_list = []
    for digit in sequence_of_numbers:
        if int(digit) % 2 == 0:
            even_list.append(int(digit))

    print(even_list)


even_numbers()
