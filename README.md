# timeago

A very simple python lib, used to format datetime with `*** time ago` statement.

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
```

or Chinese locale statement.

## Install

```sh
pip install timeago
```


## Usage & Example

```py
import timeago, datetime

now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

# locale
print (timeago.format(date, now, locale='zh_CN')) # will print 3分钟后

# input datetime
print (timeago.format(date, now)) # will print 3 minutes ago

# input date, auto add time(0, 0, 0)
print (timeago.format(datetime.date(2016, 5, 27), now))

# input date
print (timeago.format(datetime.date(2016, 5, 27), now))

# input datetime formated string
print (timeago.format('2016-05-27 12:12:12', '2016-05-27 12:12:03')) # will print just now

# locale
print (timeago.format(date, now, locale)) # will print 3分钟后
```


## Methor & Parameter

only one API **`format`**.

Three parameters of method `format`:

 - `date`: `datetime` will be done / format.
 - `now`: reference time, must be instance of `datetime`.
 - `locale`: the locale code, only zh_CN / en supported, default `en`.



## Localization

1. foke the project
2. add <locale>.py file in the locales folder.
3. pull a request.