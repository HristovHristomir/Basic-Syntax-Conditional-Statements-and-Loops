single_string = input().split()
count_of_shuffle = int(input())

for shuffle in range(count_of_shuffle):
    final_deck = []
    middle_of_the_deck = len(single_string) // 2
    left_part = single_string[0:middle_of_the_deck]
    right_part = single_string[middle_of_the_deck::]
    for index_of_the_cards in range(len(left_part)):
        final_deck.append(left_part[index_of_the_cards])
        final_deck.append((right_part[index_of_the_cards]))
    single_string = final_deck

print(final_deck)
