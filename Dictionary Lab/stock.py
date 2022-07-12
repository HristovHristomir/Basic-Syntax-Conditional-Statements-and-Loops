stock = input().split()
search = input().split()

stock_dict = {stock[i]: stock[i + 1] for i in range(0, len(stock), 2)}

for item in search:
    if item in stock_dict:
        print(f'We have {stock_dict[item]} of {item} left')
    else:
        print(f'Sorry, we don\'t have {item}')

