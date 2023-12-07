import functools


def count_cards(hand):
    res = {}
    for card in hand:
        if card in res:
            res[card] += 1
        else:
            res[card] = 1
    return res

def card_compare(c1, c2):
    order = '23456789TJQKA'
    for i in range(len(c1[0])):
        if order.index(c1[0][i]) > order.index(c2[0][i]):
            return 1
        elif order.index(c1[0][i]) < order.index(c2[0][i]):
            return -1
    return 0

def determine_rank(hand):
    c = count_cards(hand[0])
    if len(c) == 1:
        return 0
    if len(c) == 5:
        return 6
    if len(c) == 2:
        for q in c:
            if c[q] == 4:
                return 1
            if c[q] == 3:
                return 2
    if (len(c) == 3):
        for q in c:
            if c[q] == 3:
                return 3
        return 4
    if (len(c) == 4):
        return 5

with open('input') as f:
    lines = f.readlines()

hands = []

ranks = [[] for _ in range(7)]

for line in lines:
    line = line.strip()
    hands.append(line.split())
    ranks[determine_rank(hands[-1])].append(hands[-1])
    for i in range(len(ranks)):
        ranks[i].sort(key=functools.cmp_to_key(card_compare), reverse=True)

flattened = [item for sublist in ranks for item in sublist]

count = len(flattened)
total = 0

for i in flattened:
    total += count * int(i[1])
    count -= 1
print(total)