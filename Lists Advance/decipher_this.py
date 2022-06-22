secret_message = input().split()
final_secret_message = []

for word in secret_message:
    number = ''
    current_word = ''
    for letter in word:
        if letter.isdigit():
            number += letter
        else:
            break
    word = word.replace(number, '')
    number = int(number)
    current_word += chr(number)
    if len(word) >= 2:
        word = word[-1] + word[1:-1] + word[0]
    print(current_word + word, end=' ')
