words = input().split(' ')
result = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in result:
        result[word_lower] = 0
    result[word_lower] += 1

for key, value in result.items():
    if value % 2 != 0:
        print(key, end=' ')

