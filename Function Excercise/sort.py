sequence_of_numbers = input().split()


def sorting():
    num_list = list(map(int, sequence_of_numbers))
    num_list.sort()

    print(num_list)


sorting()
