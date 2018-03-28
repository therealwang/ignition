# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:36:12 2018

@author: yuwan
"""

import HandScorer as hs
from functools import total_ordering
    
HAND_SIZE = 5
suits = 'cdhs'
ranks = 'AKQJT98765432'  


def sortHand(h):
    return sorted(h, key = lambda w: [hs.ranks.index(c) for c in w])
    


@total_ordering
class Hand:
    def __init__(self, l):
        if len(l) != HAND_SIZE:
            raise ValueError('Invalid Number of Cards: {}'.format(len(l)))
        self.hand = sortHand([c[0] for c in l])
        self.suits = set([c[1] for c in l])
        self.cleanedHand = ''.join(self.hand) + ('s' if len(self.suits) == 1 else 'o')
        
    def __gt__(self, other): 
        #should we say a hand is greater if the score is less? seems more intuitive
        return hs.scoreHand(self.cleanedHand) < hs.scoreHand(other.cleanedHand)
    
    def __eq__(self, other):
        return hs.scoreHand(self.cleanedHand) == hs.scoreHand(other.cleanedHand)

