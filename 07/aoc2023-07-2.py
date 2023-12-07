import functools
from colorama import Fore

order = 'J23456789TQKA'

rank_dict = {
    0: 'Five of a kind',
    1: 'Four of a kind',
    2: 'Full house',
    3: 'Three of a kind',
    4: 'Two pairs',
    5: 'One pair',
    6: 'High card'
}

def count_cards(hand):
    res = {}
    for card in hand:
        if card in res:
            res[card] += 1
        else:
            res[card] = 1
    return res

def card_compare(c1, c2):
    for i in range(len(c1[0])):
        if order.index(c1[0][i]) > order.index(c2[0][i]):
            return 1
        elif order.index(c1[0][i]) < order.index(c2[0][i]):
            return -1
    return 0

def determine_rank(hand):
    c = count_cards(hand[0])
    keys = list(c.keys())
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

def joker_count(hand):
    if "J" not in count_cards(hand):
        return 0
    return count_cards(hand)["J"]

def new_determine_rank(hand):
    map = [[ 0,  1,  2,  3,  4,  5,  6],
           [ 0,  0, -1,  1,  2,  3,  5],
           [ 0, -1,  0, -1,  1,  3, -1],
           [ 0, -1,  0,  1, -1, -1, -1],
           [ 0,  0, -1, -1, -1, -1, -1],
           [ 0, -1, -1, -1, -1, -1, -1]]
    c = count_cards(hand[0])
    rank = determine_rank(hand)
    j = joker_count(hand[0])

    return(map[j][rank])
    

with open('input') as f:
    lines = f.readlines()
  
hands = []

ranks = [[] for _ in range(7)]

for line in lines:
    line = line.strip()
    hands.append(line.split())
    ranks[new_determine_rank(hands[-1])].append(hands[-1])
    for i in range(len(ranks)):
        ranks[i].sort(key=functools.cmp_to_key(card_compare), reverse=True)

flattened = [item for sublist in ranks for item in sublist]

count = len(flattened)
total = 0

for i in flattened:
    print(count, Fore.BLUE if joker_count(i[0]) > 0 else Fore.RED, rank_dict[new_determine_rank(i)], Fore.RESET, i[0])
    total += count * int(i[1])
    count -= 1
print(total)