# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:22:20 2018

@author: yuwan
"""


from collections import Counter

HAND_SIZE = 5
suits = 'cdhs'
ranks = 'AKQJT98765432'
rankmap = {r: ranks.index(r) for r in ranks}

handranks = {0: 'Straight Flush',
             1: 'Four of a Kind',
             2: 'Full House',
             3: 'Flush',
             4: 'Straight',
             5: 'Three of a Kind',
             6: 'Two Pair',
             7: 'One Pair',
             8: 'High Card'
             }

cardCountDict = {
            (1,4): 1,
            (2,3): 2,
            (1,1,3): 5,
            (1,2,2): 6,
            (1,1,1,2): 7,
            (1,1,1,1,1): 8
        }

allHands = []
temp = [''] * 5

def addNextCard(hand):
    global allHands
    if len(hand)==5:
        if hand != hand[0] * 5:
            allHands.append(hand + 'o')
        return
    for card in ranks[ranks.index(hand[-1]):]:
        addNextCard(hand + card)

def addFlush(hand):
    global allHands
    if len(hand)==5:
        if hand != hand[0] * 5:
            allHands.append(hand + 's')
        return
    for card in ranks[ranks.index(hand[-1])+1:]:
        addFlush(hand + card)

for card in ranks:
    addNextCard(card)
    
for card in ranks:
    addFlush(card)
    
def isStraight(handNoSuit):
    curr = handNoSuit[0]
    for c in handNoSuit[1:]:
        if rankmap[c] != rankmap[curr] + 1 and not (rankmap[c] == 9 and rankmap[curr] == 0):
            return False
        curr = c
    
    return True

def scoreHand(hand):
    handNoSuit = hand[:-1]
    straight = isStraight(handNoSuit)
    flush = hand[-1] == 's'
    
    cardCounter = Counter(handNoSuit)
    sortedHand = sorted(cardCounter.keys(), 
            key = lambda card: (cardCounter[card],13 -ranks.index(card)),
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
        score = [cardCountDict[cardCounts]]
        
    if straight and sortedHand[0] == 'A' and sortedHand[1] == '5':
        sortedHand = sortedHand[1:]
    score += [ranks.index(card) for card in sortedHand]
    return score
                
allHands = sorted(allHands, key = scoreHand)    
