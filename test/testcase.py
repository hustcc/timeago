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

    def test_raw_timedelta_defaults_to_now(self):
        delta = datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(delta, None), '10 seconds ago')

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
        # Just now.
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=4)
        self.assertEqual(timeago.format(date, now, locale), 'только что')

        # Seconds.
        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), '10 секунд назад')

        now = date + datetime.timedelta(seconds=21)
        self.assertEqual(timeago.format(date, now, locale), '21 секунду назад')

        now = date + datetime.timedelta(seconds=22)
        self.assertEqual(timeago.format(date, now, locale), '22 секунды назад')

        now = date + datetime.timedelta(seconds=26)
        self.assertEqual(timeago.format(date, now, locale), '26 секунд назад')

        # Minutes.
        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'минуту назад')

        now = date + datetime.timedelta(seconds=60 * 2)
        self.assertEqual(timeago.format(date, now, locale), '2 минуты назад')

        now = date + datetime.timedelta(seconds=60 * 5)
        self.assertEqual(timeago.format(date, now, locale), '5 минут назад')

        now = date + datetime.timedelta(seconds=60 * 21)
        self.assertEqual(timeago.format(date, now, locale), '21 минуту назад')

        now = date + datetime.timedelta(seconds=60 * 22)
        self.assertEqual(timeago.format(date, now, locale), '22 минуты назад')

        now = date + datetime.timedelta(seconds=60 * 26)
        self.assertEqual(timeago.format(date, now, locale), '26 минут назад')

        # Hours.
        now = date + datetime.timedelta(hours=1)
        self.assertEqual(timeago.format(date, now, locale), 'час назад')

        now = date + datetime.timedelta(hours=3)
        self.assertEqual(timeago.format(date, now, locale), '3 часа назад')

        now = date + datetime.timedelta(hours=5)
        self.assertEqual(timeago.format(date, now, locale), '5 часов назад')

        now = date + datetime.timedelta(hours=21)
        self.assertEqual(timeago.format(date, now, locale), '21 час назад')

        now = date + datetime.timedelta(hours=23)
        self.assertEqual(timeago.format(date, now, locale), '23 часа назад')

        # Days.
        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), 'вчера')

        now = date + datetime.timedelta(hours=24 * 3)
        self.assertEqual(timeago.format(date, now, locale), '3 дня назад')

        now = date + datetime.timedelta(hours=24 * 5)
        self.assertEqual(timeago.format(date, now, locale), '5 дней назад')

        # Weeks.
        now = date + datetime.timedelta(days=7)
        self.assertEqual(timeago.format(date, now, locale), 'неделю назад')

        for week in (2, 3, 4):
            now = date + datetime.timedelta(days=week * 7)
            self.assertEqual(timeago.format(date, now, locale), '%s недели назад' % week)

        # Months.
        now = date + datetime.timedelta(days=31)
        self.assertEqual(timeago.format(date, now, locale), 'месяц назад')

        for month in (2, 3, 4):
            now = date + datetime.timedelta(days=month * 31)
            self.assertEqual(timeago.format(date, now, locale), '%s месяца назад' % month)

        now = date + datetime.timedelta(seconds=2592000 * 5.5)
        self.assertEqual(timeago.format(date, now, locale), '5 месяцев назад')

        # Years.
        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), 'год назад')

        for year in (2, 3, 4):
            now = date + datetime.timedelta(seconds=31536000 * (year + 0.1))
            self.assertEqual(timeago.format(date, now, locale), '%s года назад' % year)

        now = date + datetime.timedelta(seconds=31536000 * 5.1)
        self.assertEqual(timeago.format(date, now, locale), '5 лет назад')

        now = date + datetime.timedelta(seconds=31536000 * 21.1)
        self.assertEqual(timeago.format(date, now, locale), '21 год назад')

        now = date + datetime.timedelta(seconds=31536000 * 22.1)
        self.assertEqual(timeago.format(date, now, locale), '22 года назад')

        now = date + datetime.timedelta(seconds=31536000 * 26.1)
        self.assertEqual(timeago.format(date, now, locale), '26 лет назад')

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

    def test_timeago_bg(self):
        locale = 'bg'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "току що")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "преди 10 секунди")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "преди 1 минута")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "преди 3 минути")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "преди 1 час")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "преди 2 часа")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "преди 1 ден")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "преди 4 дни")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "преди 1 седмица")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "преди 4 седмици")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "преди 1 месец")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "преди 3 месеца")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "преди 1 година")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "преди 2 години")

    def test_timeago_ca(self):
        locale = 'ca'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "fa un moment")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "fa 10 segons")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "fa 1 minut")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "fa 3 minuts")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "fa 1 hora")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "fa 2 hores")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "fa 1 dia")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "fa 4 dies")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "fa 1 setmana")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "fa 4 setmanes")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "fa 1 mes")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "fa 3 mesos")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "fa 1 any")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "fa 2 anys")

    def test_timeago_da(self):
        locale = 'da'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "for et øjeblik siden")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "for 10 sekunder siden")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "for 1 minut siden")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "for 3 minutter siden")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "for 1 time siden")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "for 2 timer siden")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "for 1 dag siden")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "for 4 dage siden")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "for 1 uge siden")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "for 4 uger siden")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "for 1 måned siden")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "for 3 måneder siden")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "for 1 år siden")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "for 2 år siden")

    def test_timeago_el(self):
        locale = 'el'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "μόλις τώρα")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 δευτερόλεπτα πριν")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 λεπτό πριν")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 λεπτά πριν")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 ώρα πριν")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 ώρες πριν")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 μέρα πριν")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 μέρες πριν")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 εβδομάδα πριν")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 εβδομάδες πριν")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 μήνα πριν")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 μήνες πριν")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 χρόνο πριν")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 χρόνια πριν")

    def test_timeago_en_short(self):
        locale = 'en_short'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "just now")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10s ago")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1m ago")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3m ago")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1h ago")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2h ago")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1d ago")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4d ago")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1w ago")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4w ago")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1mo ago")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3mo ago")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1yr ago")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2yr ago")

    def test_timeago_es(self):
        locale = 'es'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "justo ahora")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "hace 10 segundos")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "hace 1 minuto")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "hace 3 minutos")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "hace 1 hora")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "hace 2 horas")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "hace 1 día")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "hace 4 días")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "hace 1 semana")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "hace 4 semanas")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "hace 1 mes")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "hace 3 meses")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "hace 1 año")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "hace 2 años")

    def test_timeago_eu(self):
        locale = 'eu'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "orain")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "duela 10 segundu")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "duela minutu 1")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "duela 3 minutu")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "duela ordu 1")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "duela 2 ordu")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "duela egun 1")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "duela 4 egun")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "duela aste 1")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "duela 4 aste")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "duela hillabete 1")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "duela 3 hillabete")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "duela urte 1")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "duela 2 urte")

    def test_timeago_fi(self):
        locale = 'fi'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "juuri äsken")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 sekuntia sitten")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "minuutti sitten")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 minuuttia sitten")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "tunti sitten")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 tuntia sitten")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "päivä sitten")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 päivää sitten")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "viikko sitten")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 viikkoa sitten")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "kuukausi sitten")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 kuukautta sitten")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "vuosi sitten")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 vuotta sitten")

    def test_timeago_fr(self):
        locale = 'fr'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "à l'instant")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "il y a 10 secondes")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "il y a 1 minute")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "il y a 3 minutes")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "il y a 1 heure")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "il y a 2 heures")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "il y a 1 jour")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "il y a 4 jours")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "il y a 1 semaine")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "il y a 4 semaines")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "il y a 1 mois")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "il y a 3 mois")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "il y a 1 an")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "il y a 2 ans")

    def test_timeago_gl(self):
        locale = 'gl'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "xusto agora")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "hai 10 segundos")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "hai 1 minuto")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "hai 3 minutos")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "hai 1 hora")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "hai 2 horas")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "hai 1 día")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "hai 4 días")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "hai 1 semana")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "hai 4 semanas")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "hai 1 mes")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "hai 3 meses")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "hai 1 ano")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "hai 2 anos")

    def test_timeago_he(self):
        locale = 'he'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "זה עתה")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "לפני 10 שניות")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "לפני דקה")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "לפני 3 דקות")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "לפני שעה")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "לפני 2 שעות")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "אתמול")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "לפני 4 ימים")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "לפני שבוע")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "לפני 4 שבועות")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "לפני חודש")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "לפני 3 חודשים")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "לפני שנה")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "לפני 2 שנים")

    def test_timeago_hu(self):
        locale = 'hu'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "éppen most")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 másodperce")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 perce")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 perce")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 órája")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 órája")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 napja")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 napja")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 hete")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 hete")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 hónapja")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 hónapja")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 éve")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 éve")

    def test_timeago_in_ID(self):
        locale = 'in_ID'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "baru saja")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 detik yang lalu")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 menit yang lalu")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 menit yang lalu")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 jam yang lalu")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 jam yang lalu")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 hari yang lalu")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 hari yang lalu")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 minggu yang lalu")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 minggu yang lalu")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 bulan yang lalu")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 bulan yang lalu")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 tahun yang lalu")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 tahun yang lalu")

    def test_timeago_it(self):
        locale = 'it'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "poco fa")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 secondi fa")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "un minuto fa")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 minuti fa")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "un'ora fa")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 ore fa")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "un giorno fa")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 giorni fa")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "una settimana fa")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 settimane fa")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "un mese fa")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 mesi fa")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "un anno fa")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 anni fa")

    def test_timeago_ko(self):
        locale = 'ko'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "방금")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10초 전")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1분 전")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3분 전")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1시간 전")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2시간 전")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1일 전")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4일 전")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1주일 전")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4주일 전")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1개월 전")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3개월 전")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1년 전")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2년 전")

    def test_timeago_ml(self):
        locale = 'ml'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "ഇപ്പോള്‍")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 സെക്കന്റ്‌കള്‍ക്ക് മുന്‍പ്")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 മിനിറ്റിനു മുന്‍പ്")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 മിനിറ്റുകള്‍ക്ക് മുന്‍പ")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 മണിക്കൂറിനു മുന്‍പ്")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 മണിക്കൂറുകള്‍ക്കു മുന്‍പ്")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 ഒരു ദിവസം മുന്‍പ്")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 ദിവസങ്ങള്‍ക് മുന്‍പ്")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 ആഴ്ച മുന്‍പ്")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 ആഴ്ചകള്‍ക്ക് മുന്‍പ്")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 മാസത്തിനു മുന്‍പ്")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 മാസങ്ങള്‍ക്ക് മുന്‍പ്")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 വര്‍ഷത്തിനു  മുന്‍പ്")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 വര്‍ഷങ്ങള്‍ക്കു മുന്‍പ്")

    def test_timeago_my(self):
        locale = 'my'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "ယခုအတွင်း")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 စက္ကန့် အကြာက")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 မိနစ် အကြာက")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 မိနစ် အကြာက")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 နာရီ အကြာက")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 နာရီ အကြာက")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 ရက် အကြာက")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 ရက် အကြာက")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 ပတ် အကြာက")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 ပတ် အကြာက")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 လ အကြာက")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 လ အကြာက")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 နှစ် အကြာက")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 နှစ် အကြာက")

    def test_timeago_nb_NO(self):
        locale = 'nb_NO'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "akkurat nå")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 sekunder siden")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 minutt siden")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 minutter siden")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 time siden")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 timer siden")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 dag siden")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 dager siden")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 uke siden")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 uker siden")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 måned siden")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 måneder siden")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 år siden")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 år siden")

    def test_timeago_nl(self):
        locale = 'nl'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "recent")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 seconden geleden")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 minuut geleden")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 minuten geleden")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 uur geleden")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 uren geleden")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 dag geleden")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 dagen geleden")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 week geleden")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 weken geleden")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 maand geleden")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 maanden geleden")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 jaar geleden")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 jaren geleden")

    def test_timeago_nn_NO(self):
        locale = 'nn_NO'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "nett no")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 sekund sidan")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 minutt sidan")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 minutt sidan")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 time sidan")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 timar sidan")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 dag sidan")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 dagar sidan")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 veke sidan")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 veker sidan")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 månad sidan")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 månadar sidan")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 år sidan")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 år sidan")

    # test pl lang
    def test_timeago_pl(self):
        locale = 'pl'
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), 'właśnie teraz')

        now = date - datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), 'za chwilę')

        now = date - datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), 'za 10 sekund')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), '10 sekund temu')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), '12 sekund temu')

        now = date + datetime.timedelta(seconds=33)
        self.assertEqual(timeago.format(date, now, locale), '33 sekundy temu')

        now = date + datetime.timedelta(seconds=52)
        self.assertEqual(timeago.format(date, now, locale), '52 sekundy temu')

        now = date - datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'za minutę')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'minutę temu')

        now = date - datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), 'za 3 minuty')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), '3 minuty temu')

        now = date - datetime.timedelta(seconds=60 * 5.1)
        self.assertEqual(timeago.format(date, now, locale), 'za 5 minut')

        now = date + datetime.timedelta(seconds=60 * 5.1)
        self.assertEqual(timeago.format(date, now, locale), '5 minut temu')

        now = date - datetime.timedelta(minutes=11)
        self.assertEqual(timeago.format(date, now, locale), 'za 11 minut')

        now = date + datetime.timedelta(minutes=11)
        self.assertEqual(timeago.format(date, now, locale), '11 minut temu')

        now = date - datetime.timedelta(minutes=12)
        self.assertEqual(timeago.format(date, now, locale), 'za 12 minut')

        now = date + datetime.timedelta(minutes=12)
        self.assertEqual(timeago.format(date, now, locale), '12 minut temu')

        now = date - datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), 'za godzinę')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), 'godzinę temu')

        now = date - datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), 'za 2 godziny')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), '2 godziny temu')

        now = date - datetime.timedelta(hours=5)
        self.assertEqual(timeago.format(date, now, locale), 'za 5 godzin')

        now = date + datetime.timedelta(hours=5)
        self.assertEqual(timeago.format(date, now, locale), '5 godzin temu')

        now = date + datetime.timedelta(hours=13)
        self.assertEqual(timeago.format(date, now, locale), '13 godzin temu')

        now = date + datetime.timedelta(hours=23)
        self.assertEqual(timeago.format(date, now, locale), '23 godziny temu')

        now = date - datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), 'za 1 dzień')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), '1 dzień temu')

        now = date - datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), 'za 4 dni')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), '4 dni temu')

        now = date - datetime.timedelta(weeks=1)
        self.assertEqual(timeago.format(date, now, locale), 'za tydzień')

        now = date + datetime.timedelta(weeks=1)
        self.assertEqual(timeago.format(date, now, locale), 'tydzień temu')

        now = date - datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), 'za 4 tygodnie')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), '4 tygodnie temu')

        now = date - datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), 'za 3 miesiące')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), '3 miesiące temu')

        now = date - datetime.timedelta(seconds=2592000 * 5.5)
        self.assertEqual(timeago.format(date, now, locale), 'za 5 miesięcy')

        now = date + datetime.timedelta(seconds=2592000 * 5.5)
        self.assertEqual(timeago.format(date, now, locale), '5 miesięcy temu')

        now = date - datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), 'za rok')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), 'rok temu')

        now = date - datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), 'za 2 lata')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), '2 lata temu')

        now = date - datetime.timedelta(weeks=4.35 * 12 * 5.5)
        self.assertEqual(timeago.format(date, now, locale), 'za 5 lat')

        now = date + datetime.timedelta(weeks=4.35 * 12 * 5.5)
        self.assertEqual(timeago.format(date, now, locale), '5 lat temu')

        now = date + datetime.timedelta(weeks=4.35 * 12 * 22.5)
        self.assertEqual(timeago.format(date, now, locale), '22 lata temu')

        now = date + datetime.timedelta(weeks=4.35 * 12 * 25.5)
        self.assertEqual(timeago.format(date, now, locale), '25 lat temu')

        now = date + datetime.timedelta(weeks=4.35 * 12 * 101)
        self.assertEqual(timeago.format(date, now, locale), '101 lat temu')

        now = date + datetime.timedelta(weeks=4.35 * 12 * 102)
        self.assertEqual(timeago.format(date, now, locale), '102 lata temu')

        now = date + datetime.timedelta(weeks=4.35 * 12 * 112)
        self.assertEqual(timeago.format(date, now, locale), '112 lat temu')

        now = date + datetime.timedelta(weeks=4.35 * 12 * 122)
        self.assertEqual(timeago.format(date, now, locale), '122 lata temu')

        now = date + datetime.timedelta(weeks=4.35 * 12 * 125)
        self.assertEqual(timeago.format(date, now, locale), '125 lat temu')

    def test_timeago_pt_BR(self):
        locale = 'pt_BR'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "agora mesmo")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "há 10 segundos")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "há um minuto")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "há 3 minutos")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "há uma hora")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "há 2 horas")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "há um dia")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "há 4 dias")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "há uma semana")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "há 4 semanas")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "há um mês")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "há 3 meses")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "há um ano")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "há 2 anos")

    def test_timeago_ta(self):
        locale = 'ta'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "இப்போது")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 நொடிக்கு முன்")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 நிமிடத்திற்க்கு முன்")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 நிமிடத்திற்க்கு முன்")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 மணி நேரத்திற்கு முன்")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 மணி நேரத்திற்கு முன்")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 நாளுக்கு முன்")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 நாட்களுக்கு முன்")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 வாரத்திற்கு முன்")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 வாரங்களுக்கு முன்")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 மாதத்திற்கு முன்")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 மாதங்களுக்கு முன்")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 வருடத்திற்கு முன்")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 வருடங்களுக்கு முன்")

    def test_timeago_th(self):
        locale = 'th'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "เมื่อสักครู่นี้")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 วินาทีที่แล้ว")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 นาทีที่แล้ว")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 นาทีที่แล้ว")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 ชั่วโมงที่แล้ว")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 ชั่วโมงที่แล้ว")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 วันที่แล้ว")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 วันที่แล้ว")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 อาทิตย์ที่แล้ว")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 อาทิตย์ที่แล้ว")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 เดือนที่แล้ว")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 เดือนที่แล้ว")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 ปีที่แล้ว")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 ปีที่แล้ว")

    def test_timeago_tr(self):
        locale = 'tr'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "az önce")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 saniye önce")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 dakika önce")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 dakika önce")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 saat önce")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 saat önce")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 gün önce")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 gün önce")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 hafta önce")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 hafta önce")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 ay önce")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 ay önce")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 yıl önce")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 yıl önce")

    def test_timeago_vi(self):
        locale = 'vi'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "vừa xong")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10 giây trước")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1 phút trước")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3 phút trước")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1 giờ trước")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2 giờ trước")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1 ngày trước")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4 ngày trước")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1 tuần trước")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4 tuần trước")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1 tháng trước")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3 tháng trước")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1 năm trước")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2 năm trước")

    def test_timeago_zh_TW(self):
        locale = 'zh_TW'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), "剛剛")

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), "10秒前")

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), "1分鐘前")

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), "3分鐘前")

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), "1小時前")

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), "2小時前")

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), "1天前")

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), "4天前")

        now = date + datetime.timedelta(seconds=86400 * 7)
        self.assertEqual(timeago.format(date, now, locale), "1周前")

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), "4周前")

        now = date + datetime.timedelta(seconds=86400 * 31)
        self.assertEqual(timeago.format(date, now, locale), "1月前")

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), "3月前")

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), "1年前")

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), "2年前")

    # test ar lang
    def test_timeago_ar(self):
        locale = "ar"
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=1)
        self.assertEqual(timeago.format(date, now, locale), 'الآن')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 10 ثواني')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 12 ثانية')

        now = date + datetime.timedelta(seconds=50)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 50 ثانية')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'منذ دقيقة')

        now = date + datetime.timedelta(seconds=65)
        self.assertEqual(timeago.format(date, now, locale), 'منذ دقيقة')

        now = date + datetime.timedelta(seconds=120)
        self.assertEqual(timeago.format(date, now, locale), 'منذ دقيقتين')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 3 دقائق')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), 'منذ ساعة')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), 'منذ ساعتين')

        now = date + datetime.timedelta(seconds=3600 * 3)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 3 ساعات')

        now = date + datetime.timedelta(seconds=3600 * 4)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 4 ساعات')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), 'منذ يوم')

        now = date + datetime.timedelta(seconds=86400 * 2)
        self.assertEqual(timeago.format(date, now, locale), 'منذ يومين')

        now = date + datetime.timedelta(seconds=86400 * 3)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 3 أيام')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 4 أيام')

        now = date + datetime.timedelta(seconds=648000)
        self.assertEqual(timeago.format(date, now, locale), 'منذ أسبوع')

        now = date + datetime.timedelta(seconds=648000 * 2)
        self.assertEqual(timeago.format(date, now, locale), 'منذ أسبوعين')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 4 أسابيع')

        now = date + datetime.timedelta(seconds=2592000 * 1.5)
        self.assertEqual(timeago.format(date, now, locale), 'منذ شهر')

        now = date + datetime.timedelta(seconds=2592000 * 2.5)
        self.assertEqual(timeago.format(date, now, locale), 'منذ شهرين')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 3 أشهر')

        now = date + datetime.timedelta(seconds=2592000 * 10.5)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 10 أشهر')

        now = date + datetime.timedelta(seconds=2592000 * 11.5)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 11 شهراً')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), 'منذ سنة')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), 'منذ سنة')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), 'منذ سنتين')

        now = date + datetime.timedelta(seconds=31536000 * 3.1)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 3 سنوات')

        now = date + datetime.timedelta(seconds=31536000 * 11.1)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 11 سنة')

        now = date + datetime.timedelta(seconds=31536000 * 100.1)
        self.assertEqual(timeago.format(date, now, locale), 'منذ 100 سنة')

        now = date - datetime.timedelta(seconds=1)
        self.assertEqual(timeago.format(date, now, locale), 'خلال لحظات')

        now = date - datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 10 ثواني')

        now = date - datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 12 ثانية')

        now = date - datetime.timedelta(seconds=50)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 50 ثانية')

        now = date - datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'خلال دقيقة')

        now = date - datetime.timedelta(seconds=65)
        self.assertEqual(timeago.format(date, now, locale), 'خلال دقيقة')

        now = date - datetime.timedelta(seconds=120)
        self.assertEqual(timeago.format(date, now, locale), 'خلال دقيقتين')

        now = date - datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 3 دقائق')

        now = date - datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), 'خلال ساعة')

        now = date - datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), 'خلال ساعتين')

        now = date - datetime.timedelta(seconds=3600 * 3)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 3 ساعات')

        now = date - datetime.timedelta(seconds=3600 * 4)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 4 ساعات')

        now = date - datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), 'خلال يوم')

        now = date - datetime.timedelta(seconds=86400 * 2)
        self.assertEqual(timeago.format(date, now, locale), 'خلال يومين')

        now = date - datetime.timedelta(seconds=86400 * 3)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 3 أيام')

        now = date - datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 4 أيام')

        now = date - datetime.timedelta(seconds=648000)
        self.assertEqual(timeago.format(date, now, locale), 'خلال أسبوع')

        now = date - datetime.timedelta(seconds=648000 * 2)
        self.assertEqual(timeago.format(date, now, locale), 'خلال أسبوعين')

        now = date - datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 4 أسابيع')

        now = date - datetime.timedelta(seconds=2592000 * 1.5)
        self.assertEqual(timeago.format(date, now, locale), 'خلال شهر')

        now = date - datetime.timedelta(seconds=2592000 * 2.5)
        self.assertEqual(timeago.format(date, now, locale), 'خلال شهرين')

        now = date - datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 3 أشهر')

        now = date - datetime.timedelta(seconds=2592000 * 10.5)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 10 أشهر')

        now = date - datetime.timedelta(seconds=2592000 * 11.5)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 11 شهراً')

        now = date - datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), 'خلال سنة')

        now = date - datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), 'خلال سنة')

        now = date - datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), 'خلال سنتين')

        now = date - datetime.timedelta(seconds=31536000 * 3.1)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 3 سنوات')

        now = date - datetime.timedelta(seconds=31536000 * 11.1)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 11 سنة')

        now = date - datetime.timedelta(seconds=31536000 * 100.1)
        self.assertEqual(timeago.format(date, now, locale), 'خلال 100 سنة')


    def test_timeago_uk(self):
        locale = 'uk'
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), 'щойно')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), '10 секунд тому')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), '12 секунд тому')

        now = date + datetime.timedelta(seconds=22)
        self.assertEqual(timeago.format(date, now, locale), '22 секунди тому')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'хвилину тому')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), '3 хвилини тому')

        now = date + datetime.timedelta(seconds=60 * 13)
        self.assertEqual(timeago.format(date, now, locale), '13 хвилин тому')

        now = date + datetime.timedelta(seconds=60 * 23)
        self.assertEqual(timeago.format(date, now, locale), '23 хвилини тому')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), 'годину тому')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), '2 години тому')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), 'вчора')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), '4 дні тому')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), '4 тиждні тому')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), '3 місяці тому')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), 'рік тому')

        now = date + datetime.timedelta(seconds=31536000 * 21.1)
        self.assertEqual(timeago.format(date, now, locale), '21 рік тому')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), '2 роки тому')

        now = date + datetime.timedelta(seconds=31536000 * 100)
        self.assertEqual(timeago.format(date, now, locale), '100 років тому')

    def test_timeago_lt(self):
        locale = 'lt'
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds=2)
        self.assertEqual(timeago.format(date, now, locale), 'ką tik')

        now = date + datetime.timedelta(seconds=10)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 10 sekundžių')

        now = date + datetime.timedelta(seconds=12)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 12 sekundžių')

        now = date + datetime.timedelta(seconds=60)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 1 minutę')

        now = date + datetime.timedelta(seconds=60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 3 minutes')

        now = date + datetime.timedelta(seconds=3600)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 1 valandą')

        now = date + datetime.timedelta(seconds=3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 2 valandas')

        now = date + datetime.timedelta(seconds=3600 * 15)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 15 valandų')

        now = date + datetime.timedelta(seconds=3600 * 20)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 20 valandų')

        now = date + datetime.timedelta(seconds=3600 * 22)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 22 valandas')

        now = date + datetime.timedelta(seconds=86400)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 1 dieną')

        now = date + datetime.timedelta(seconds=86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 4 dienas')

        now = date + datetime.timedelta(seconds=2592000)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 4 savaites')

        now = date + datetime.timedelta(seconds=2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 3 mėnesius')

        now = date + datetime.timedelta(seconds=31536000)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 1 metus')

        now = date + datetime.timedelta(seconds=31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 1 metus')

        now = date + datetime.timedelta(seconds=31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 2 metus')

        now = date + datetime.timedelta(seconds=31536000 * 10.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 10 metų')

        now = date + datetime.timedelta(seconds=31536000 * 17.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 17 metų')

        now = date + datetime.timedelta(seconds=31536000 * 20.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 20 metų')

        now = date + datetime.timedelta(seconds=31536000 * 28.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 28 metus')

        now = date + datetime.timedelta(seconds=31536000 * 103.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 103 metus')

        now = date + datetime.timedelta(seconds=31536000 * 110.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 110 metų')

        now = date + datetime.timedelta(seconds=31536000 * 111.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 111 metų')

        now = date + datetime.timedelta(seconds=31536000 * 125.1)
        self.assertEqual(timeago.format(date, now, locale), 'prieš 125 metus')


if __name__ == '__main__':
    unittest.main()
