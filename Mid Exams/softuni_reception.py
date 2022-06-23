import math

first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())
time = 0

students_per_hour = first_employee + second_employee + third_employee


for i in range(1, 1000000):
    if students_count == 0:
        break
    if students_per_hour == 0:
        break
    if i % 4 == 0:
        time += 1
        continue
    else:
        students_count -= students_per_hour
        time += 1
        if students_count <= 0:
            break

print(f'Time needed: {time:.0f}h.')
