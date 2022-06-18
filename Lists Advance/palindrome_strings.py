words = input().split()
palindrome = input()

result_list = []
count = 0

for word in words:
    if word[::-1] == word:
        result_list.append(word)
    if word == palindrome:
        count += 1

print(result_list)
print(f'Found palindrome {count} times')
