#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018-11-11

@author: marcel-odya
'''


def parse_pl_grammar(index, ago_in, diff_seconds):
    '''Uses the 3rd and 4th field of the list in every 2 entries - 
    the ones containing %s, if the diff ends with 2, 3 or 4 but
    not with 12, 13 or 14. 
    '''
    last_number = int(str(diff_seconds)[-1])
    last_two_numbers = None
    if diff_seconds >= 10:
        last_two_numbers = int(str(diff_seconds)[-2:])

    if ((
            (
                last_two_numbers
                and last_two_numbers not in range(12, 15)
                and last_number in range(2, 5)
            )                               # Ends with 2-5 but not with 12-15
            or diff_seconds in range(2, 5)  # or diff > 1 & < 5
        )
        and not (index + 1) % 2):           # Every 2nd line with %s
        # We choose the 3rd or 4th field for such numbers as ago_in is 0 or 1
        ago_in += 2

    return ago_in


# The functions should take in 3 parameters: list index, ago_in and diff_seonds
SPECIFIC_GRAMMAR_LANGUAGES = {
    'pl': parse_pl_grammar
}
