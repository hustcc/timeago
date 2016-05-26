#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016-5-26

@author: hustcc
'''

from __future__ import absolute_import

from datetime import datetime
from timeago.setting import SECONDS, MINUTE_SECONDS, HOUR_SECONDS, DAY_SECONDS, MONTH_SECONDS, YEAR_SECONDS
from timeago.locales import timeago_template
from timeago.excepts import ParameterUnvalid

__version__ = '1.0.1'
__license__ = 'MIT'
__ALL__ = ['format']


def format(date, now=None, locale='en'):
    '''
    the entry method
    '''
    if now is None:
        now = datetime.now()

    if type(date) != datetime or type(now) != datetime:
        raise ParameterUnvalid('the 1st, 2st parameter show be type of datetime.')

    # the gap sec
    diff_seconds = (now - date).total_seconds()

    # less then SECONDS
    if(diff_seconds < SECONDS):
        return timeago_template('JUST_NOW', locale)

    # seconds ago
    if(diff_seconds < MINUTE_SECONDS):
        return timeago_template('SECOND_AGO', locale) % (int(diff_seconds))

    # a minute ago
    if(diff_seconds < MINUTE_SECONDS * 2):
        return timeago_template('A_MINUTE_AGO', locale)

    # minutes ago
    if(diff_seconds < HOUR_SECONDS):
        return timeago_template('MINUTES_AGO', locale) % (int(diff_seconds / MINUTE_SECONDS))

    # an hour ago
    if(diff_seconds < HOUR_SECONDS * 2):
        return timeago_template('AN_HOUR_AGO', locale)

    # hours ago
    if(diff_seconds < HOUR_SECONDS * 24):
        return timeago_template('HOURS_AGO', locale) % (int(diff_seconds / HOUR_SECONDS))

    # a day ago
    if(diff_seconds < DAY_SECONDS * 2):
        return timeago_template('A_DAY_AGO', locale)

    # days ago
    if(diff_seconds < DAY_SECONDS * 30):
        return timeago_template('DAYS_AGO', locale) % (int(diff_seconds / DAY_SECONDS))

    # a month ago
    if(diff_seconds < MONTH_SECONDS * 2):
        return timeago_template('A_MONTH_AGO', locale)

    # months ago
    if(diff_seconds < MONTH_SECONDS * 12):
        return timeago_template('MONTHS_AGO', locale) % (int(diff_seconds / MONTH_SECONDS))

    # a year ago
    if(diff_seconds < YEAR_SECONDS * 2):
        return timeago_template('A_YEAR_AGO', locale)

    # years ago
    return timeago_template('YEARS_AGO', locale) % (int(diff_seconds / YEAR_SECONDS))
