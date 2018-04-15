# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:38:38 2018

@author: yuwan
"""

import HandScorer as hs
from Hand import DECK
import random
import numpy as np


def Moments(board, hole, n_iters = 10, n_hands = 9):
    ranks = []
    newDeck = set(DECK)
    for i in board+hole:
        newDeck.remove(i)
    newDeck = list(newDeck)
    
    for _ in range(n_iters):
        random.shuffle(newDeck)
        hands = [newDeck[2*i:2*i+2] for i in range(n_hands+1)]
        all7hands = [board+hole+hands[0]] + [board + hands[0] + hands[i] for i in range(1, n_hands+1)]
        scores = [hs.score7Hand(h) for  h in all7hands]
        temp = scores[0]
        ranks.append((sorted(scores, reverse = True).index(temp)+1.)/(n_hands+1))
        
    return np.mean(ranks), np.std(ranks)
    