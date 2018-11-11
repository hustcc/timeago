#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018-11-11

@author: marcel-odya
'''


def parse_pl_grammar(index, ago_in, diff_seconds):
    '''Uses the 3rd and 4th field of the list in every 2 entries - the ones containing %s,
    if the diff ends with 2, 3 or 4. '''
    last_two_numbers = None
    if diff_seconds >= 10:
        last_two_numbers = int(str(diff_seconds)[-2:])
    last_number = int(str(diff_seconds)[-1])
    if (((
          last_two_numbers and last_two_numbers not in range(12, 15) 
          and last_number in range(2, 5)
         ) 
         or (diff_seconds in range(2, 5)) # diff > 1 & < 5
        )
        and not (index + 1) % 2 # Not the line with %s

    ):
        ago_in += 2

    return ago_in


# The functions should take in 3 parameters: locale list index, ago_in and diff_seonds
SPECIFIC_GRAMMAR_LANGUAGES = {
    'pl': parse_pl_grammar
}
