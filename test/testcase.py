#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月26日

@author: hustcc
'''
import unittest
import datetime
import timeago
from timeago.excepts import ParameterUnvalid

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
    
    # test en lang
    def test_timeago_en(self):
        locale = None
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds = 2)
        self.assertEqual(timeago.format(date, now, locale), 'just now', '')
        
        now = date + datetime.timedelta(seconds = 10)
        self.assertEqual(timeago.format(date, now, locale), '10 seconds ago', '')
        
        now = date + datetime.timedelta(seconds = 12)
        self.assertEqual(timeago.format(date, now, locale), '12 seconds ago', '')
        
        now = date + datetime.timedelta(seconds = 60)
        self.assertEqual(timeago.format(date, now, locale), '1 minute ago', '')
        
        now = date + datetime.timedelta(seconds = 60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), '3 minutes ago', '')
        
        now = date + datetime.timedelta(seconds = 3600)
        self.assertEqual(timeago.format(date, now, locale), '1 hour ago', '')
        
        now = date + datetime.timedelta(seconds = 3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), '2 hours ago', '')
        
        now = date + datetime.timedelta(seconds = 86400)
        self.assertEqual(timeago.format(date, now, locale), '1 day ago', '')
        
        now = date + datetime.timedelta(seconds = 86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), '4 days ago', '')
        
        now = date + datetime.timedelta(seconds = 2592000)
        self.assertEqual(timeago.format(date, now, locale), '1 month ago', '')
        
        now = date + datetime.timedelta(seconds = 2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), '3 months ago', '')
        
        now = date + datetime.timedelta(seconds = 31536000)
        self.assertEqual(timeago.format(date, now, locale), '1 year ago', '')
        
        now = date + datetime.timedelta(seconds = 31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), '1 year ago', '')
        
        now = date + datetime.timedelta(seconds = 31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), '2 years ago', '')
    
    def test_timeago_cn(self):
        locale = 'zh_CN'
        date = datetime.datetime.now()
        now = date + datetime.timedelta(seconds = 2)
        self.assertEqual(timeago.format(date, now, locale), u'刚刚', '')
        
        now = date + datetime.timedelta(seconds = 10)
        self.assertEqual(timeago.format(date, now, locale), u'10 秒前', '')
        
        now = date + datetime.timedelta(seconds = 12)
        self.assertEqual(timeago.format(date, now, locale), u'12 秒前', '')
        
        now = date + datetime.timedelta(seconds = 60)
        self.assertEqual(timeago.format(date, now, locale), u'1 分钟前', '')
        
        now = date + datetime.timedelta(seconds = 60 * 3.4)
        self.assertEqual(timeago.format(date, now, locale), u'3 分钟前', '')
        
        now = date + datetime.timedelta(seconds = 3600)
        self.assertEqual(timeago.format(date, now, locale), u'1 小时前', '')
        
        now = date + datetime.timedelta(seconds = 3600 * 2)
        self.assertEqual(timeago.format(date, now, locale), u'2 小时前', '')
        
        now = date + datetime.timedelta(seconds = 86400)
        self.assertEqual(timeago.format(date, now, locale), u'1 天前', '')
        
        now = date + datetime.timedelta(seconds = 86400 * 4.5)
        self.assertEqual(timeago.format(date, now, locale), u'4 天前', '')
        
        now = date + datetime.timedelta(seconds = 2592000)
        self.assertEqual(timeago.format(date, now, locale), u'1 月前', '')
        
        now = date + datetime.timedelta(seconds = 2592000 * 3.5)
        self.assertEqual(timeago.format(date, now, locale), u'3 月前', '')
        
        now = date + datetime.timedelta(seconds = 31536000)
        self.assertEqual(timeago.format(date, now, locale), u'1 年前', '')
        
        now = date + datetime.timedelta(seconds = 31536000 * 1.1)
        self.assertEqual(timeago.format(date, now, locale), u'1 年前', '')
        
        now = date + datetime.timedelta(seconds = 31536000 * 2.1)
        self.assertEqual(timeago.format(date, now, locale), u'2 年前', '')
    
if __name__ =='__main__':
    unittest.main()