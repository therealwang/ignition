# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:22:20 2018

@author: yuwan
"""


from collections import Counter, defaultdict

HAND_SIZE = 5
SUITS = 'cdhs'
RANKS = 'AKQJT98765432'
RANKMAP = {r: RANKS.index(r) for r in RANKS}

HAND_RANKS = {0: 'Straight Flush',
             1: 'Four of a Kind',
             2: 'Full House',
             3: 'Flush',
             4: 'Straight',
             5: 'Three of a Kind',
             6: 'Two Pair',
             7: 'One Pair',
             8: 'High Card'
             }

CARD_COUNT_DICT = {
            (1,4): 1,
            (2,3): 2,
            (1,1,3): 5,
            (1,2,2): 6,
            (1,1,1,2): 7,
            (1,1,1,1,1): 8
        }

ALL_HANDS = []


def addNextCard(hand):
    global ALL_HANDS
    if len(hand)==HAND_SIZE:
        if hand != hand[0] * HAND_SIZE:
            ALL_HANDS.append(hand + 'o')
        return
    for card in RANKS[RANKS.index(hand[-1]):]:
        addNextCard(hand + card)

def addFlush(hand):
    global ALL_HANDS
    if len(hand)==HAND_SIZE:
        if hand != hand[0] * HAND_SIZE:
            ALL_HANDS.append(hand + 's')
        return
    for card in RANKS[RANKS.index(hand[-1])+1:]:
        addFlush(hand + card)

for card in RANKS:
    addNextCard(card)
    
for card in RANKS:
    addFlush(card)

    
def isStraight(hand_no_suit):
    curr = hand_no_suit[0]
    for c in hand_no_suit[1:]:
        if RANKMAP[c] != RANKMAP[curr] + 1 and not (RANKMAP[c] == 9 and RANKMAP[curr] == 0):
            return False
        curr = c
    
    return True

def scoreHand(hand):
    hand_no_suit = hand[:-1]
    straight = isStraight(hand_no_suit)
    flush = hand[-1] == 's'
    
    cardCounter = Counter(hand_no_suit)
    sortedHand = sorted(cardCounter.keys(), 
            key = lambda card: (cardCounter[card],13 -RANKS.index(card)),
            reverse = True
            )
    cardCounts = tuple(sorted(cardCounter.values()))
    
    if straight and flush:
        score = [0]
    elif straight:
        score = [4]
    elif flush:
        score = [3]
    else:
        score = [CARD_COUNT_DICT[cardCounts]]
        
    if straight and sortedHand[0] == 'A' and sortedHand[1] == '5':
        sortedHand = sortedHand[1:]
    score += [RANKS.index(card) for card in sortedHand]
    return score
                
ALL_HANDS = sorted(ALL_HANDS, key = scoreHand)    
ALL_HANDS_DICT = {hand: ALL_HANDS.index(hand) for hand in ALL_HANDS}
ALL_HANDS_DICT[''] = float('inf')

'''
Attempt to create a dict of mappings from 7 card hands
'''
def findStraight(vals_list):
    new_list = [vals_list[0]]
    for v in vals_list[1:]:
        if v != new_list[-1]:
            new_list.append(v)
    if len(new_list) < 5:
        return ''
    longest_straight = [1]
    for c1, c2 in zip(new_list, new_list[1:]):
        if RANKMAP[c1] == RANKMAP[c2] - 1:
            longest_straight.append(min(longest_straight[-1] + 1,5))
        elif (RANKMAP[new_list[0]] == 0 and RANKMAP[c2] == 9):
            longest_straight.append(2)
        else:
            longest_straight.append(1)
            
    if 5 not in longest_straight:
        return ''
    else:
        ind = longest_straight.index(5)
        if new_list[ind] == '2':
            if new_list[ind-4] != '6':
                return ''.join([new_list[0]] + new_list[ind-3:ind+1])
        return ''.join(new_list[ind-4:ind+1])
                        
    
    
def make7Hand(hand_list):
    suits = defaultdict(lambda: [])
    vals = defaultdict(lambda: 0)
    
    for h in hand_list:
        v, s = h
        vals[v] += 1
        suits[s].append(v)
        
    return vals, suits

def score7Hand(hand_list):
    vals, suits = make7Hand(hand_list)
    uniquevals = sorted(vals.keys(), key = RANKMAP.get)
    cands = []
    candstr = findStraight(uniquevals)
    if candstr != '':
        cands.append(candstr + 'o')
    candvals = sorted(vals.items(), key = lambda card: (vals[card[0]], 13-RANKS.index(card[0])), reverse = True)
    candvals = ''.join([v * count for v, count in candvals])
    candvals = candvals[:5]
    candvals = ''.join(sorted(candvals, key = RANKMAP.get)) + 'o'
    cands.append(candvals)
    for s in suits:
        temp = findStraight(suits[s])
        if temp !=  '':
            cands.append(temp + 's')
    candscores = [ALL_HANDS_DICT[c] for c in cands]
    return min(candscores)


