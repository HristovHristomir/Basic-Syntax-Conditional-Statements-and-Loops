number_of_rooms = int(input())
count_free_chairs = 0
flag = True

for num in range(1, number_of_rooms + 1):
    chair = input().split()
    if len(chair[0]) < int(chair[1]):
        more_chair = int(chair[1]) - len(chair[0])
        flag = False
        print(f'{more_chair} more chairs needed in room {num}')
    elif len(chair[0]) > int(chair[1]):
        count_free_chairs += len(chair[0]) - int(chair[1])

if flag is True:
    print(f'Game On, {count_free_chairs} free chairs left')
