# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:58:34 2018

@author: yuwan
"""

import pandas as pd

def parseFile(filepath):
    f = open(filepath, 'r')
    while True:
        parseHand(f)
    
    
def parseHand(f):
    f.readline()
    nextline = f.readline()
    playermap = dict()
    while nextline.startswith('Seat'):
        nll = nextline.split()
        num = int(nll[1][0])
        pos = nll[2]
        playermap[pos] = num
        nextline = f.readline()
    seattopos = {v: ((v-playermap['Small']) % 6) for v in playermap.values()}
    possiblepos = sorted(list(seattopos.values()))
    seattopos = {k: possiblepos.index(v) for k, v in seattopos.items()}
    return seattopos, playermap
        
        
class Player:
    def __init__(self):
       pass 
    
filepath = 'C:\\Ignition\\Hand History\\14167489\\HH20180325-141122 - 5814033 - RING - $0.10-$0.25 - HOLDEM - NL - TBL No.14766355.txt'
