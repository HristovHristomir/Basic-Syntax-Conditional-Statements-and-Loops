number_of_people = int(input())
elevator_capacity = int(input())

if (number_of_people % elevator_capacity) != 0:
    courses = (number_of_people / elevator_capacity) + 1
    print(int(courses))
else:
    courses = number_of_people / elevator_capacity
    print(int(courses))
