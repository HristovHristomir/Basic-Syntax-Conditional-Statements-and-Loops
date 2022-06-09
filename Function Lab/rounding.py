first_list = list(map(float, input().split()))
round_list = []


def rounded():
    for i in first_list:
        i = round(i, 0)
        round_list.append(int(i))
    return round_list


print(rounded())
