# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:36:12 2018

@author: yuwan
"""


from functools import total_ordering
import HandScorer as hs
from HandScorer import ALL_HANDS_DICT
    
HAND_SIZE = 5
SUITS = 'cdhs'
RANKS = 'AKQJT98765432'  
RANKMAP = {r: RANKS.index(r) for r in RANKS}


def sortHand(h):
    return sorted(h, key = lambda w: [RANKMAP[c] for c in w])
    


@total_ordering
class Hand:
    def __init__(self, l):
        if len(l) != HAND_SIZE:
            raise ValueError('Invalid Number of Cards: {}'.format(len(l)))
        self.hand = sortHand([c[0] for c in l])
        self.suits = set([c[1] for c in l])
        self.cleaned_hand = ''.join(self.hand) + ('s' if len(self.suits) == 1 else 'o')
        
    def __gt__(self, other): 
        #should we say a hand is greater if the score is less? seems more intuitive
        return ALL_HANDS_DICT[self.cleaned_hand] < ALL_HANDS_DICT[other.cleaned_hand]
    
    def __eq__(self, other):
        return ALL_HANDS_DICT[self.cleaned_hand] == ALL_HANDS_DICT[other.cleaned_hand]
