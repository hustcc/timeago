#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2019-12-19

@author: ANJD
'''

base = [
    ["الآن", "خلال لحظات"],
    ["منذ ثانيتين", "خلال ثانيتين", "منذ %s ثواني", "خلال %s ثواني", "منذ %s ثانية", "خلال %s ثانية"],
    ["منذ دقيقة", "خلال دقيقة"],
    ["منذ دقيقتين", "خلال دقيقتين", "منذ %s دقائق", "خلال %s دقائق", "منذ %s دقيقة", "خلال %s دقيقة"],
    ["منذ ساعة", "خلال ساعة"],
    ["منذ ساعتين", "خلال ساعتين", "منذ %s ساعات", "خلال %s ساعات", "منذ %s ساعة", "خلال %s ساعة"],
    ["منذ يوم", "خلال يوم"],
    ["منذ يومين", "خلال يومين", "منذ %s أيام", "خلال %s أيام", "منذ %s يوم", "خلال %s يوم"],
    ["منذ أسبوع", "خلال أسبوع"],
    ["منذ أسبوعين", "خلال أسبوعين", "منذ %s أسابيع", "خلال %s أسابيع", "منذ %s أسبوع", "خلال %s أسبوع"],
    ["منذ شهر", "خلال شهر"],
    ["منذ شهرين", "خلال شهرين", "منذ %s أشهر", "خلال %s أشهر", "منذ %s شهراً", "خلال %s شهراً"],
    ["منذ سنة", "خلال سنة"],
    ["منذ سنتين", "خلال سنتين", "منذ %s سنوات", "خلال %s سنوات", "منذ %s سنة", "خلال %s سنة"]
]


def generate(row, y):
    def formatting(time):
        '''
        Uses the 3rd and 4th field of the list in every 2 entries -
        the ones containing %s, if the diff ends with 2, 3 or 4 but
        not with 12, 13 or 14.
        '''
        if row % 2 == 0:
            return base[row][y]

        if time == 2:
            return base[row][y]

        if time in range(3, 11):
            return base[row][y + 2]

        return base[row][y + 4]

    return formatting


LOCALE = generate
