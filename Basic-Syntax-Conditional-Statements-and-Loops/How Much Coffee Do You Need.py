string = ''

coffee = 0

while string != 'END':
    string = input()
    if string == 'END':
        break
    if string.islower():
        if string == 'coding' or string == 'dog' or string == 'cat' or string == 'movie':
            coffee += 1
    elif string.isupper():
        if string == 'CODING' or string == 'DOG' or string == 'CAT' or string == 'MOVIE':
            coffee += 2

if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)
