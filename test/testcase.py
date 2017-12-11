#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月26日

@author: hustcc
'''

import sys
import os
# We need to add the source to the path (required at least on my machine).
sys.path.insert(0, os.path.realpath('src'))

import unittest
import datetime
import random
from datetime import date as dateimport, time
import timeago
from timeago.excepts import ParameterUnvalid
from timeago import parser


def datetime_to_string(d):
    temp = ['%s-%s-%s %s:%s:%s',
            '%s/%s/%s %s:%s:%s'][(random.randint(1, 99)) % 2]
    return temp % (d.year, d.month, d.day, d.hour, d.minute, d.second)


class TestCase(unittest.TestCase):
    # init
    def setUp(self):
        unittest.TestCase.setUp(self)

    # exit
    def tearDown(self):
        pass

    # test except
    def test_timeago_except(self):
        date = ''
        self.assertRaises(ParameterUnvalid, timeago.format, date)

        date = '12:23:23a'
        self.assertRaises(ParameterUnvalid, timeago.format, date)

        date = '2016-5-27  12:23:23'
        self.assertRaises(ParameterUnvalid, timeago.format, date)

    # test en lang
    def test_timeago_en(self):
        locale = None
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), 'just now')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), '10 seconds ago')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), '12 seconds ago')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), '1 minute ago')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), '3 minutes ago')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), '1 hour ago')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), '2 hours ago')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), '1 day ago')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), '4 days ago')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), '4 weeks ago')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), '3 months ago')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), '1 year ago')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), '1 year ago')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), '2 years ago')

    # test fa lang
    def test_timeago_fa(self):
        locale = 'fa_IR'
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), 'هم اکنون')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), '10 ثانیه پیش')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), '12 ثانیه پیش')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'یک دقیقه پیش')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), '3 دقیقه پیش')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), 'یک ساعت پیش')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), '2 ساعت پیش')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), 'دیروز')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), '4 روز پیش')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), '4 هفته پیش')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), '3 ماه پیش')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), 'پارسال')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), 'پارسال')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), '2 سال پیش')

    def test_timeago_cn(self):
        locale = 'zh_CN'
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), u'刚刚')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), u'10秒前')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), u'12秒前')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), u'1分钟前')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), u'3分钟前')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), u'1小时前')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), u'2小时前')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), u'1天前')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), u'4天前')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), u'4周前')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), u'3月前')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), u'1年前')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), u'1年前')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), u'2年前')

    # test ja lang
    def test_timeago_ja(self):
        locale = 'ja'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), u'たった今')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), u'10秒前')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), u'12秒前')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), u'1分前')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), u'3分前')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), u'1時間前')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), u'2時間前')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), u'昨日')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), u'4日前')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), u'4週間前')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), u'3ヶ月前')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), u'1年前')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), u'1年前')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), u'2年前')

    # test in
    def test_timeago_en_in(self):
        locale = 'en'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(now, date, locale), 'a while')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(now, date, locale), 'in 10 seconds')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(now, date, locale), 'in 12 seconds')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 minute')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(now, date, locale), 'in 3 minutes')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 hour')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(now, date, locale), 'in 2 hours')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 day')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(now, date, locale), 'in 4 days')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(now, date, locale), 'in 4 weeks')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(now, date, locale), 'in 3 months')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 year')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 year')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(now, date, locale), 'in 2 years')

    # test in
    def test_timeago_fa_in(self):
        locale = 'fa_IR'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(now, date, locale), 'به زودی')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(now, date, locale), '10 ثانیه بعد')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(now, date, locale), '12 ثانیه بعد')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(now, date, locale), 'یک دقیقه بعد')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(now, date, locale), '3 دقیقه بعد')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(now, date, locale), 'یک ساعت بعد')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(now, date, locale), '2 ساعت بعد')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(now, date, locale), 'فردا')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(now, date, locale), '4 روز بعد')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(now, date, locale), '4 هفته بعد')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(now, date, locale), '3 ماه بعد')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(now, date, locale), 'سال بعد')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(now, date, locale), 'سال بعد')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(now, date, locale), '2 سال بعد')

    def test_timeago_cn_in(self):
        locale = 'zh_CN'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(now, date, locale), u'片刻后')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(now, date, locale), u'10秒后')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(now, date, locale), u'12秒后')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(now, date, locale), u'1分钟后')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(now, date, locale), u'3分钟后')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(now, date, locale), u'1小时后')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(now, date, locale), u'2小时后')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(now, date, locale), u'1天后')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(now, date, locale), u'4天后')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(now, date, locale), u'4周后')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(now, date, locale), u'3月后')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(now, date, locale), u'1年后')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(now, date, locale), u'1年后')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(now, date, locale), u'2年后')

    # test ja lang in
    def test_timeago_ja_in(self):
        locale = 'ja'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(now, date, locale), u'すぐに')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(now, date, locale), u'10秒以内')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(now, date, locale), u'12秒以内')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(now, date, locale), u'1分以内')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(now, date, locale), u'3分以内')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(now, date, locale), u'1時間以内')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(now, date, locale), u'2時間以内')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(now, date, locale), u'1日以内')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(now, date, locale), u'4日以内')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(now, date, locale), u'4週間以内')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(now, date, locale), u'3ヶ月以内')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(now, date, locale), u'1年以内')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(now, date, locale), u'1年以内')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(now, date, locale), u'2年以内')

    # test ru lang
    def test_timeago_ru(self):
        locale = 'ru'
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), 'только что')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), '10 секунд назад')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), '12 секунд назад')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'минуту назад')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), '3 минут назад')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), 'час назад')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), '2 часов назад')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), 'вчера')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), '4 дней назад')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), '4 недель назад')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), '3 месяцев назад')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), 'год назад')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), 'год назад')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), '2 лет назад')

        # test ja lang

    def test_timeago_de(self):
        locale = 'de'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), u'gerade eben')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), u'vor 10 Sekunden')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), u'vor 1 Minute')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), u'vor 3 Minuten')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), u'vor einer Stunde')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), u'vor 2 Stunden')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), u'vor 1 Tag')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), u'vor 4 Tagen')

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), u'vor 1 Woche')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), u'vor 4 Wochen')

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), u'vor 1 Monat')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), u'vor 3 Monaten')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), u'vor 1 Jahr')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), u'vor 2 Jahren')

    # test en lang
    def test_timeago_parse_input(self):
        date = datetime.datetime(2016, 5, 27, 21, 22, 2)

        # datetime string
        input = '2016-05-27 21:22:02'
        self.assertEqual(parser.parse(input), date)

        input = '2016-5-27 21:22:2'
        self.assertEqual(parser.parse(input), date)

        input = '2016/05/27 21:22:02'
        self.assertEqual(parser.parse(input), date)

        input = '2016/5/27 21:22:02'
        self.assertEqual(parser.parse(input), date)

        date = datetime.datetime(2016, 5, 27, 0, 0, 0)
        input = '2016/05/27'
        self.assertEqual(parser.parse(input), date)

        input = '2016-5-27'
        self.assertEqual(parser.parse(input), date)

        input = '2016-05-27'
        self.assertEqual(parser.parse(input), date)

        today = dateimport.today()
        date = datetime.datetime(
            today.year, today.month, today.day, 12, 12, 12)
        input = '12:12:12'
        self.assertEqual(parser.parse(input), date)

        # date
        input = dateimport(2016, 5, 27)
        date = datetime.datetime(2016, 5, 27, 0, 0, 0)
        self.assertEqual(parser.parse(input), date)

        # time
        today = dateimport.today()
        input = time(21, 45, 27)
        date = datetime.datetime(
            today.year, today.month, today.day, 21, 45, 27)
        self.assertEqual(parser.parse(input), date)

        # datetime
        input = datetime.datetime(2016, 5, 27, 21, 45, 27)
        date = datetime.datetime(2016, 5, 27, 21, 45, 27)
        self.assertEqual(parser.parse(input), date)

        # None
        input = '2016-05-27 23.23:21'
        self.assertEqual(parser.parse(input), None)

        # None
        input = '2016-05-27  23:23:21'
        self.assertEqual(parser.parse(input), None)

    # test en lang
    def test_timeago_string_input(self):
        locale = None
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), 'just now')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(datetime_to_string(
            date), datetime_to_string(now), locale), '10 seconds ago')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '12 seconds ago')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '1 minute ago')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '3 minutes ago')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '1 hour ago')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '2 hours ago')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '1 day ago')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '4 days ago')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '4 weeks ago')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '3 months ago')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '1 year ago')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '1 year ago')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(
            datetime_to_string(date), now, locale), '2 years ago')

    # test en lang
    def test_timeago_delta(self):
        locale = None
        date = datetime.timedelta(seconds=9)
        self.assertEqual(timeago.format(date, None, locale), 'just now')


if __name__ == '__main__':
    unittest.main()
