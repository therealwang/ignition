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
    
    
def parseHand(file):
    f.readline()
    nextline = f.readline()
    while nextline.startswith('Seat'):
        
        
class Player:
    def __init__(self):
        
    
filepath = 'C:\\Ignition\\Hand History\\14167489\\HH20180325-141122 - 5814033 - RING - $0.10-$0.25 - HOLDEM - NL - TBL No.14766355.txt'
