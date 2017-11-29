# timeago

A very simple python lib, used to format datetime with `*** time ago` statement. Javascript version here. [timeago.js](https://github.com/hustcc/timeago.js).

[![Build Status](https://travis-ci.org/hustcc/timeago.svg?branch=master)](https://travis-ci.org/hustcc/timeago) [![PyPi Status](https://img.shields.io/pypi/v/timeago.svg)](https://pypi.python.org/pypi/timeago) [![Python Versions](https://img.shields.io/pypi/pyversions/timeago.svg)](https://pypi.python.org/pypi/timeago) [![PyPi Downloads](https://img.shields.io/pypi/dm/timeago.svg)](https://pypi.python.org/pypi/timeago)

Such as: 

```
just now
12 seconds ago
3 minutes ago
2 hours ago
24 days ago
6 months ago
2 years ago

in 12 seconds
in 3 minutes
in 2 hours
in 24 days
in 6 months
in 2 years
```

or Chinese locale statement.

## Install

```sh
pip install timeago
```


## Usage & Example

```py
# -*- coding: utf-8 -*-
import timeago, datetime

now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

date = datetime.datetime.now()

# locale
print (timeago.format(date, now, 'zh_CN')) # will print `3分钟前`

# input datetime
print (timeago.format(date, now)) # will print 3 minutes ago

# input timedelta
print (timeago.format(datetime.timedelta(seconds = 60 * 3.4))) # will print 3 minutes ago

# input date, auto add time(0, 0, 0)
print (timeago.format(datetime.date(2016, 5, 27), now))

# input datetime formated string
print (timeago.format('2016-05-27 12:12:03', '2016-05-27 12:12:12')) # will print just now

# inverse two parameters
print (timeago.format('2016-05-27 12:12:12', '2016-05-27 12:12:03')) # will print a while

```


## Method & Parameter

only one API **`format`**.

Three parameters of method `format`:

 - **`date`**: the parameter which will be formated, must be instance of `datetime` / `timedelta` or datetime formated string.
 - **`now`**: reference time, must be instance of `datetime` or datetime formated string.
 - **`locale`**: the locale code, default `en`. 


## Locale

At the time we're speaking, [following locale](src/timeago/locales) are available:
 - `en`
 - `fa_IR`
 - `in_BG`
 - `in_HI`
 - `ja`
 - `ru`
 - `sv_SE`
 - `zh_CN`
 - `de`


## Localization

1. Fork the project
2. Create a locale python script called `[name_of_your_locale].py` following the existing other locales.
3. Add the name of your locale in the Readme to keep it updated.
4. Add test case following the [english model](/test/testcase.py#L44)
5. Create the Pull Request.
