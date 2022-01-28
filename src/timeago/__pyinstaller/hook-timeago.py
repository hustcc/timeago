#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2022-01-28

@author: alexitx
'''

_locales = (
    'ar',
    'bg',
    'ca',
    'da',
    'de',
    'el',
    'en_short',
    'en',
    'es',
    'eu',
    'fa_IR',
    'fi',
    'fr',
    'gl',
    'guj_IN',
    'he',
    'hu',
    'in_BG',
    'in_HI',
    'in_ID',
    'is',
    'it',
    'ja',
    'ko',
    'lt',
    'ml',
    'my',
    'nb_NO',
    'nl',
    'nn_NO',
    'pl',
    'pt_BR',
    'pt_PT',
    'ro',
    'ru',
    'sv_SE',
    'ta',
    'th',
    'tr',
    'uk',
    'vi',
    'zh_CN',
    'zh_TW'
)


hiddenimports = [f'timeago.locales.{locale}' for locale in _locales]
