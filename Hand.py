# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:36:12 2018

@author: yuwan
"""

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
        if rankmap[c] != rankmap[curr] + 1:
            return False
        curr = c
    
    return True

def scoreHand(hand):
    straight = isStraight(hand[:-1])
    
    



def sortHand(h):
    return sorted(h, key = lambda w: [ranks.index(c) for c in w])
    



class Hand:
    def __init__(self, l):
        if len(l) != 5:
            raise ValueError('Invalid Number of Cards: {}'.format(len(l)))
        self.hand = sortHand([c[0] for c in l])
        self.suits = set([c[1] for c in l])
        

