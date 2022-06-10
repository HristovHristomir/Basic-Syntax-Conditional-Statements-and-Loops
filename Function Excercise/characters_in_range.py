char1 = input()
char2 = input()


def char_in_range():
    for i in range(ord(char1) + 1, ord(char2)):
        print(chr(i), end=' ')


char_in_range()
