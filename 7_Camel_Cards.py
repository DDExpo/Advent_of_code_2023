from collections import Counter


# Part Two: switch priority of 'J'
VALUES_CARDS: dict[str: int] = {key: val for key, val in zip('AKQT98765432J',
                                                             range(13, 0, -1))}


def sort_type_card_in_place(cards: list[tuple[str, int]]) -> list[tuple[int,
                                                                        int]]:

    cards.sort(key=lambda x: (VALUES_CARDS[x[0][0]], VALUES_CARDS[x[0][1]],
                              VALUES_CARDS[x[0][2]], VALUES_CARDS[x[0][3]],
                              VALUES_CARDS[x[0][4]]))
    return cards


def sort_cards(cards: list[str]) -> list[tuple[int, int]]:

    cards_types: list[list[tuple[str, int]]] = [[], [], [], [], [], [], []]

    for card_bid in cards:
        card, bid = card_bid.split()
        counted_card = Counter(card)

        # Part Two
        if 0 < counted_card.get('J', 0) < 5:
            for _ in range(counted_card.pop('J')):
                counted_card[counted_card.most_common(1)[0][0]] += 1

        most_common_card = counted_card.most_common(1)[0][1]
        if most_common_card >= 5:
            cards_types[6].append((card, int(bid)))
        elif most_common_card == 4:
            cards_types[5].append((card, int(bid)))
        elif most_common_card == 3:
            if counted_card.most_common(2)[1][1] == 2:
                cards_types[4].append((card, int(bid)))
            else:
                cards_types[3].append((card, int(bid)))
        elif most_common_card == 2:
            if counted_card.most_common(2)[1][1] == 2:
                cards_types[2].append((card, int(bid)))
            else:
                cards_types[1].append((card, int(bid)))
        else:
            cards_types[0].append((card, int(bid)))

    for card_type in cards_types:
        sort_type_card_in_place(card_type)

    return cards_types


file = open('Advent_of_code_2023/data/input_day_7.txt',
            'r').read().splitlines()

sorted_cards: list[tuple[int, int]] = sort_cards(file)

result: int = 0
index: int = 0

for type_card in sorted_cards:
    for card_bid in type_card:
        index += 1
        result += card_bid[1] * index

print(result)
