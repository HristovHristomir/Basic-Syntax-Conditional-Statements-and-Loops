list_of_chars = input().split(', ')

ascii_dict = {key: ord(key) for key in list_of_chars}

print(ascii_dict)
