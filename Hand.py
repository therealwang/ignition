# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:36:12 2018

@author: yuwan
"""

HAND_SIZE = 5
suits = 'cdhs'
ranks = 'AKQJT98765432'
alphabet = '23456789TJQKAcdhs'
alphabet = {k: v for k, v in zip(alphabet, range(len(alphabet)))}

allHands = []
temp = [''] * 5

def addNextCard(hand):
    global allHands
    if len(hand)==5:
        if hand != hand[0] * 5:
            allHands.append(hand)
        return
    for card in ranks[ranks.index(hand[-1]):]:
        addNextCard(hand + card)

for card in ranks:
    addNextCard(card)
    

def sortHand(h):
    return sorted(h, key = lambda w: [alphabet.get(c, ord(c)) for c in w])
    

class Hand:
    def __init__(self, l):
        if len(l) != 5:
            raise ValueError('Invalid Number of Cards: {}'.format(len(l)))
        self.hand = sortHand(l)

