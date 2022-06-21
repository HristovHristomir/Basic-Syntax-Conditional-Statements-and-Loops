number_of_electron = int(input())
flag = True
result = []
num = 1

while flag is True:
    shell = 2 * num**2
    result.append(shell)
    num += 1
    number_of_electron -= shell
    if number_of_electron <= 0:
        number_of_electron += shell
        result.pop()
        result.append(number_of_electron)
        break

print(result)
