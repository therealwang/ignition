# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:22:20 2018

@author: yuwan
"""


from collections import Counter

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
