#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016-5-26

@author: hustcc
'''

from datetime import datetime, timedelta
from timeago.locales import timeago_template
from timeago.excepts import ParameterUnvalid
from timeago import parser

__version__ = '1.0.5'
__license__ = 'MIT'
__ALL__ = ['format']


# Original fix #2 for Py2.6
def total_seconds(dt):
    # Keep backward compatibility with Python 2.6 which doesn't have
    # this method
    if hasattr(datetime, 'total_seconds'):
        return dt.total_seconds()
    else:
        return (dt.microseconds + (dt.seconds + dt.days * 24 * 3600) * 10**6) / 10**6


# second, minite, hour, day, week, month, year(365 days)
SEC_ARRAY = [60, 60, 24, 7, 365.0 / 7 / 12, 12]
SEC_ARRAY_LEN = 6


def format(date, now=None, locale='en'):
    '''
    the entry method
    '''
    if isinstance(date, timedelta):
        diff_seconds = int(total_seconds(date))
    else:
        if now is None:
            now = datetime.now()
        date = parser.parse(date)
        now = parser.parse(now)

        if date is None:
            raise ParameterUnvalid('the parameter `date` should be datetime / timedelta, or datetime formated string.')
        if now is None:
            raise ParameterUnvalid('the parameter `now` should be datetime, or datetime formated string.')
        # the gap sec
        diff_seconds = int(total_seconds(now - date))

    # is ago or in
    ago_in = 0
    if diff_seconds < 0:
        ago_in = 1  # date is later then now, is the time in future
        diff_seconds *= -1  # chango to positive

    tmp = 0
    for i in xrange(SEC_ARRAY_LEN):
        tmp = SEC_ARRAY[i]
        if diff_seconds > tmp:
            diff_seconds /= tmp
    diff_seconds = int(diff_seconds)
    i *= 2

    if diff_seconds > (i == 0 and 9 or 1):
        i += 1

    return timeago_template(locale, i, ago_in).replace('%s', diff_seconds, 1)
