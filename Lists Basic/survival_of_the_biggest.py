import math

list_of_integers = input().split()
count_of_n = int(input())
int_list = [int(i) for i in list_of_integers]
count_of_n_flag = True

while count_of_n_flag:
    temp = min(int_list)
    int_list.remove(temp)
    count_of_n -= 1
    if count_of_n == 0:
        count_of_n_flag = False

print(*int_list, sep=', ')
