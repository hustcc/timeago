#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月26日

@author: hustcc
'''
import unittest
import datetime, random
from datetime import date as dateimport, time

import timeago
from timeago.excepts import ParameterUnvalid
from timeago import parser

def datetime_to_string(d):
    temp = ['%s-%s-%s %s:%s:%s', '%s/%s/%s %s:%s:%s'][(random.randint(1, 99)) % 2]
    return temp % (d.year, d.month, d.day, d.hour, d.minute, d.second)

class TestCase(unittest.TestCase):
    ## init
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
        now = date + datetime.timedelta(seconds = 2)
        self.assertEqual(timeago.format(date, now, locale), 'just now')
        
        now = date + datetime.timedelta(seconds = 10)
        self.assertEqual(timeago.format(date, now, locale), '10 seconds ago')
        
        now = date + datetime.timedelta(seconds = 12)
        self.assertEqual(timeago.format(date, now, locale), '12 seconds ago')
        
        now = date + datetime.timedelta(seconds = 60)
        self.assertEqual(timeago.format(date, now, locale), '1 minute ago')
        
        now = date + datetime.timedelta(seconds = 60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), '3 minutes ago')
        
        now = date + datetime.timedelta(seconds = 3600)
        self.assertEqual(timeago.format(date, now, locale), '1 hour ago')
        
        now = date + datetime.timedelta(seconds = 3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), '2 hours ago')
        
        now = date + datetime.timedelta(seconds = 86400)
        self.assertEqual(timeago.format(date, now, locale), '1 day ago')
        
        now = date + datetime.timedelta(seconds = 86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), '4 days ago')
        
        now = date + datetime.timedelta(seconds = 2592000)
        self.assertEqual(timeago.format(date, now, locale), '1 month ago')
        
        now = date + datetime.timedelta(seconds = 2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), '3 months ago')
        
        now = date + datetime.timedelta(seconds = 31536000)
        self.assertEqual(timeago.format(date, now, locale), '1 year ago')
        
        now = date + datetime.timedelta(seconds = 31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), '1 year ago')
        
        now = date + datetime.timedelta(seconds = 31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), '2 years ago')
    
    def test_timeago_cn(self):
        locale = 'zh_CN'
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds = 2)
        self.assertEqual(timeago.format(date, now, locale), u'刚刚')
        
        now = date + datetime.timedelta(seconds = 10)
        self.assertEqual(timeago.format(date, now, locale), u'10秒前')
        
        now = date + datetime.timedelta(seconds = 12)
        self.assertEqual(timeago.format(date, now, locale), u'12秒前')
        
        now = date + datetime.timedelta(seconds = 60)
        self.assertEqual(timeago.format(date, now, locale), u'1分钟前')
        
        now = date + datetime.timedelta(seconds = 60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), u'3分钟前')
        
        now = date + datetime.timedelta(seconds = 3600)
        self.assertEqual(timeago.format(date, now, locale), u'1小时前')
        
        now = date + datetime.timedelta(seconds = 3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), u'2小时前')
        
        now = date + datetime.timedelta(seconds = 86400)
        self.assertEqual(timeago.format(date, now, locale), u'1天前')
        
        now = date + datetime.timedelta(seconds = 86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), u'4天前')
        
        now = date + datetime.timedelta(seconds = 2592000)
        self.assertEqual(timeago.format(date, now, locale), u'1月前')
        
        now = date + datetime.timedelta(seconds = 2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), u'3月前')
        
        now = date + datetime.timedelta(seconds = 31536000)
        self.assertEqual(timeago.format(date, now, locale), u'1年前')
        
        now = date + datetime.timedelta(seconds = 31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), u'1年前')
        
        now = date + datetime.timedelta(seconds = 31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), u'2年前')
    
    # test in
    def test_timeago_en_in(self):
        locale = 'en'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds = 2)
        self.assertEqual(timeago.format(now, date, locale), 'a while')
        
        now = date + datetime.timedelta(seconds = 10)
        self.assertEqual(timeago.format(now, date, locale), 'in 10 seconds')
        
        now = date + datetime.timedelta(seconds = 12)
        self.assertEqual(timeago.format(now, date, locale), 'in 12 seconds')
        
        now = date + datetime.timedelta(seconds = 60)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 minute')
        
        now = date + datetime.timedelta(seconds = 60 * 3.4)
        self.assertEqual(timeago.format(now, date, locale), 'in 3 minutes')
        
        now = date + datetime.timedelta(seconds = 3600)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 hour')
        
        now = date + datetime.timedelta(seconds = 3600 * 2)
        self.assertEqual(timeago.format(now, date, locale), 'in 2 hours')
        
        now = date + datetime.timedelta(seconds = 86400)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 day')
        
        now = date + datetime.timedelta(seconds = 86400 * 4.5)
        self.assertEqual(timeago.format(now, date, locale), 'in 4 days')
        
        now = date + datetime.timedelta(seconds = 2592000)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 month')
        
        now = date + datetime.timedelta(seconds = 2592000 * 3.5)
        self.assertEqual(timeago.format(now, date, locale), 'in 3 months')
        
        now = date + datetime.timedelta(seconds = 31536000)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 year')
        
        now = date + datetime.timedelta(seconds = 31536000 * 1.1)
        self.assertEqual(timeago.format(now, date, locale), 'in 1 year')
        
        now = date + datetime.timedelta(seconds = 31536000 * 2.1)
        self.assertEqual(timeago.format(now, date, locale), 'in 2 years')

    def test_timeago_cn_in(self):
        locale = 'zh_CN'

        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds = 2)
        self.assertEqual(timeago.format(now, date, locale), u'片刻后')
        
        now = date + datetime.timedelta(seconds = 10)
        self.assertEqual(timeago.format(now, date, locale), u'10秒后')
        
        now = date + datetime.timedelta(seconds = 12)
        self.assertEqual(timeago.format(now, date, locale), u'12秒后')
        
        now = date + datetime.timedelta(seconds = 60)
        self.assertEqual(timeago.format(now, date, locale), u'1分钟后')
        
        now = date + datetime.timedelta(seconds = 60 * 3.4)
        self.assertEqual(timeago.format(now, date, locale), u'3分钟后')
        
        now = date + datetime.timedelta(seconds = 3600)
        self.assertEqual(timeago.format(now, date, locale), u'1小时后')
        
        now = date + datetime.timedelta(seconds = 3600 * 2)
        self.assertEqual(timeago.format(now, date, locale), u'2小时后')
        
        now = date + datetime.timedelta(seconds = 86400)
        self.assertEqual(timeago.format(now, date, locale), u'1天后')
        
        now = date + datetime.timedelta(seconds = 86400 * 4.5)
        self.assertEqual(timeago.format(now, date, locale), u'4天后')
        
        now = date + datetime.timedelta(seconds = 2592000)
        self.assertEqual(timeago.format(now, date, locale), u'1月后')
        
        now = date + datetime.timedelta(seconds = 2592000 * 3.5)
        self.assertEqual(timeago.format(now, date, locale), u'3月后')
        
        now = date + datetime.timedelta(seconds = 31536000)
        self.assertEqual(timeago.format(now, date, locale), u'1年后')
        
        now = date + datetime.timedelta(seconds = 31536000 * 1.1)
        self.assertEqual(timeago.format(now, date, locale), u'1年后')
        
        now = date + datetime.timedelta(seconds = 31536000 * 2.1)
        self.assertEqual(timeago.format(now, date, locale), u'2年后')

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
        print (parser.parse(input))
        self.assertEqual(parser.parse(input), date)

        input = '2016-5-27'
        self.assertEqual(parser.parse(input), date)

        input = '2016-05-27'
        self.assertEqual(parser.parse(input), date)

        today = dateimport.today()
        date = datetime.datetime(today.year, today.month, today.day, 12, 12, 12)
        input = '12:12:12'
        self.assertEqual(parser.parse(input), date)

        # date
        input = dateimport(2016, 5, 27)
        date = datetime.datetime(2016, 5, 27, 0, 0, 0)
        self.assertEqual(parser.parse(input), date)
        
        # time
        today = dateimport.today()
        input = time(21, 45, 27)
        date = datetime.datetime(today.year, today.month, today.day, 21, 45, 27)
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
        now = date + datetime.timedelta(seconds = 2)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), 'just now')
        
        now = date + datetime.timedelta(seconds = 10)
        self.assertEqual(timeago.format(datetime_to_string(date), datetime_to_string(now), locale), '10 seconds ago')
        
        now = date + datetime.timedelta(seconds = 12)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '12 seconds ago')
        
        now = date + datetime.timedelta(seconds = 60)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '1 minute ago')
        
        now = date + datetime.timedelta(seconds = 60 * 3.4)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '3 minutes ago')
        
        now = date + datetime.timedelta(seconds = 3600)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '1 hour ago')
        
        now = date + datetime.timedelta(seconds = 3600 * 2)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '2 hours ago')
        
        now = date + datetime.timedelta(seconds = 86400)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '1 day ago')
        
        now = date + datetime.timedelta(seconds = 86400 * 4.5)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '4 days ago')
        
        now = date + datetime.timedelta(seconds = 2592000)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '1 month ago')
        
        now = date + datetime.timedelta(seconds = 2592000 * 3.5)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '3 months ago')
        
        now = date + datetime.timedelta(seconds = 31536000)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '1 year ago')
        
        now = date + datetime.timedelta(seconds = 31536000 * 1.1)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '1 year ago')
        
        now = date + datetime.timedelta(seconds = 31536000 * 2.1)
        self.assertEqual(timeago.format(datetime_to_string(date), now, locale), '2 years ago')
    
    # test en lang
    def test_timeago_delta(self):
        locale = None
        date = datetime.timedelta(seconds = 9)
        self.assertEqual(timeago.format(date, None, locale), 'just now')
        

if __name__ =='__main__':
    unittest.main()