password = input()


def pass_validator():
    validator = False
    check = True
    count_nums = 0
    if 6 <= len(password) <= 10:
        validator = True
    else:
        print('Password must be between 6 and 10 characters')
        check = False
    for index in password:
        if index.isdigit() or index.isalpha():
            validator = True
        else:
            validator = False
            print('Password must consist only of letters and digits')
            check = False
            break
    for count in password:
        if count.isdigit():
            count_nums += 1
    if count_nums >= 2:
        validator = True
    else:
        validator = False
        print('Password must have at least 2 digits')
    if not check:
        validator = False
    return validator


if pass_validator() is True:
    print('Password is valid')
