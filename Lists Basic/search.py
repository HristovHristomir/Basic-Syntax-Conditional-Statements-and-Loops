n = int(input())
word = input()

first_list = []
last_list = []

for i in range(n):
    string = input()
    first_list.append(string)

for i in range(len(first_list)):
    if word in first_list[i]:
        last_list.append(first_list[i])

print(first_list)
print(last_list)
