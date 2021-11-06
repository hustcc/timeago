#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021-11-6

@author: jenca-adam
'''

base = [
    ["práve teraz", "pred chvíľou"],
    ["pred %s sekundami", "o %s sekúnd","o %s sekundy"],
    ["pred minútou", "o minútu"],
    ["pred %s minútami", "o %s minút","o %s minúty"],
    ["pred hodinou", "o hodinu"],
    ["pred %s hodinami", "o %s hodín","o %s hodiny"],
    ["pred dňom", "o deň"],
    ["pred %s dňami", "o %s dni"],
    ["pred týždňom", "o týždeň"],
    ["pred %s týždňami", "o %s týždňov","o %s týždne"],
    ["pred mesiacom", "o mesiac"],
    ["pred %s mesiacmi", "o %s mesiacov","o %s mesiace"],
    ["pred rokom", "o rok"],
    ["pred %s rokmi", "o %s rokov","o %s roky"],
]
def generate(row,y):
    def formatting(time):
        if y==1 and time<5:
                try:
                    
                    return base[row][y+1]
                except IndexError:
                    pass
        return base[row][y]
    return formatting
LOCALE=generate
    
