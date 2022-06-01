n = int(input())

positive = []
negative = []
count_of_positive = 0
sum_of_negative = 0

for i in range(n):
    num = int(input())
    if num >= 0:
        count_of_positive += 1
        positive.append(num)
    else:
        sum_of_negative += num
        negative.append(num)

print(positive)
print(negative)
print(f'Count of positives: {count_of_positive}')
print(f'Sum of negatives: {sum_of_negative}')
